/**
 * LEGAL CROSSWORD ENGINE (V3.0 Phase 3)
 * Manages grid layout, cell navigation, direction toggling, active word highlighting,
 * letter input, verification, hint penalties, and scoring.
 */
(function() {
  'use strict';

  class CrosswordEngine {
    constructor(puzzleData) {
      this.puzzle = puzzleData;
      this.rows = puzzleData.gridSize.rows;
      this.cols = puzzleData.gridSize.cols;
      
      this.grid = [];
      this.activeRow = -1;
      this.activeCol = -1;
      this.direction = 'across'; // 'across' or 'down'
      this.activeWord = null;
      
      this.hintsUsed = 0;
      this.lettersRevealed = 0;
      this.wordsRevealed = 0;
      this.penalties = 0;
      this.errorsMade = 0;
      
      this.startTime = Date.now();
      this.completed = false;
      this.completedWords = new Set();
      
      this._initGrid();
    }

    _initGrid() {
      // Create empty rows x cols grid
      this.grid = [];
      for (let r = 0; r < this.rows; r++) {
        const row = [];
        for (let c = 0; c < this.cols; c++) {
          row.push({
            row: r,
            col: c,
            isBlocked: true,
            solution: '',
            userChar: '',
            clueNum: null,
            acrossWord: null,
            downWord: null,
            isRevealed: false,
            isCorrect: false,
            isError: false
          });
        }
        this.grid.push(row);
      }

      // Populate from puzzle words
      this.puzzle.words.forEach(w => {
        const wordStr = w.word.toUpperCase().replace(/\s+/g, '');
        const r = w.row;
        const c = w.col;
        const dir = w.direction.toLowerCase();
        
        // Mark starting clue number
        if (!this.grid[r][c].clueNum) {
          this.grid[r][c].clueNum = w.clueNum;
        }

        for (let i = 0; i < wordStr.length; i++) {
          const currR = dir === 'across' ? r : r + i;
          const currC = dir === 'across' ? c + i : c;
          const cell = this.grid[currR][currC];
          
          cell.isBlocked = false;
          cell.solution = wordStr[i];
          
          if (dir === 'across') {
            cell.acrossWord = w;
          } else {
            cell.downWord = w;
          }
        }
      });

      // Default select the first playable cell
      this.selectFirstCell();
    }

    selectFirstCell() {
      if (this.puzzle.words.length > 0) {
        const firstW = this.puzzle.words[0];
        this.selectClue(firstW.clueNum, firstW.direction);
      }
    }

    selectCell(r, c) {
      if (r < 0 || r >= this.rows || c < 0 || c >= this.cols) return;
      const cell = this.grid[r][c];
      if (cell.isBlocked) return;

      // If clicked on current cell, toggle direction if both exist
      if (this.activeRow === r && this.activeCol === c) {
        if (cell.acrossWord && cell.downWord) {
          this.toggleDirection();
          return;
        }
      }

      this.activeRow = r;
      this.activeCol = c;

      // Ensure direction aligns with available words
      if (this.direction === 'across' && !cell.acrossWord && cell.downWord) {
        this.direction = 'down';
      } else if (this.direction === 'down' && !cell.downWord && cell.acrossWord) {
        this.direction = 'across';
      }

      this._updateActiveWord();
    }

    toggleDirection() {
      const cell = this.getActiveCell();
      if (!cell) return;
      
      if (this.direction === 'across' && cell.downWord) {
        this.direction = 'down';
      } else if (this.direction === 'down' && cell.acrossWord) {
        this.direction = 'across';
      }
      this._updateActiveWord();
    }

    selectClue(clueNum, dir) {
      const targetWord = this.puzzle.words.find(w => w.clueNum === clueNum && w.direction.toLowerCase() === dir.toLowerCase());
      if (!targetWord) return;

      this.direction = targetWord.direction.toLowerCase();
      this.activeRow = targetWord.row;
      this.activeCol = targetWord.col;
      this._updateActiveWord();
    }

    _updateActiveWord() {
      const cell = this.getActiveCell();
      if (!cell || cell.isBlocked) {
        this.activeWord = null;
        return;
      }
      this.activeWord = this.direction === 'across' ? cell.acrossWord : cell.downWord;
    }

    getActiveCell() {
      if (this.activeRow < 0 || this.activeCol < 0) return null;
      return this.grid[this.activeRow][this.activeCol];
    }

    getWordCells(wordObj) {
      if (!wordObj) return [];
      const cells = [];
      const len = wordObj.word.length;
      const r = wordObj.row;
      const c = wordObj.col;
      const dir = wordObj.direction.toLowerCase();

      for (let i = 0; i < len; i++) {
        const currR = dir === 'across' ? r : r + i;
        const currC = dir === 'across' ? c + i : c;
        cells.push(this.grid[currR][currC]);
      }
      return cells;
    }

    enterLetter(char) {
      const cell = this.getActiveCell();
      if (!cell || cell.isBlocked || cell.isRevealed) return;

      const upper = char.toUpperCase().replace(/[^A-Z]/g, '');
      if (!upper) return;

      cell.userChar = upper;
      cell.isError = false;

      // Check if current active word was just completed
      this._checkActiveWordCompletion();

      // Move forward to next cell in current word
      this.moveCursorForward();
    }

    backspace() {
      const cell = this.getActiveCell();
      if (!cell || cell.isBlocked) return;

      if (cell.userChar !== '' && !cell.isRevealed) {
        cell.userChar = '';
        cell.isError = false;
      } else {
        // Move back and erase
        this.moveCursorBackward();
        const prev = this.getActiveCell();
        if (prev && !prev.isRevealed) {
          prev.userChar = '';
          prev.isError = false;
        }
      }
    }

    moveCursor(dRow, dCol) {
      let r = this.activeRow + dRow;
      let c = this.activeCol + dCol;

      while (r >= 0 && r < this.rows && c >= 0 && c < this.cols) {
        if (!this.grid[r][c].isBlocked) {
          this.activeRow = r;
          this.activeCol = c;
          this._updateActiveWord();
          return;
        }
        r += dRow;
        c += dCol;
      }
    }

    moveCursorForward() {
      if (!this.activeWord) return;
      const cells = this.getWordCells(this.activeWord);
      const currIdx = cells.findIndex(c => c.row === this.activeRow && c.col === this.activeCol);
      if (currIdx !== -1 && currIdx < cells.length - 1) {
        const next = cells[currIdx + 1];
        this.activeRow = next.row;
        this.activeCol = next.col;
      }
    }

    moveCursorBackward() {
      if (!this.activeWord) return;
      const cells = this.getWordCells(this.activeWord);
      const currIdx = cells.findIndex(c => c.row === this.activeRow && c.col === this.activeCol);
      if (currIdx > 0) {
        const prev = cells[currIdx - 1];
        this.activeRow = prev.row;
        this.activeCol = prev.col;
      }
    }

    _checkActiveWordCompletion() {
      if (!this.activeWord) return;
      const cells = this.getWordCells(this.activeWord);
      const isFilled = cells.every(c => c.userChar !== '');
      if (isFilled) {
        const isMatch = cells.every(c => c.userChar === c.solution);
        if (isMatch) {
          cells.forEach(c => c.isCorrect = true);
          this.completedWords.add(`${this.activeWord.clueNum}-${this.activeWord.direction}`);
        }
      }
    }

    /**
     * Reveals the current active letter with 15 points penalty
     */
    revealLetter() {
      const cell = this.getActiveCell();
      if (!cell || cell.isBlocked || cell.isRevealed) return null;

      cell.userChar = cell.solution;
      cell.isRevealed = true;
      cell.isCorrect = true;
      cell.isError = false;

      this.hintsUsed++;
      this.lettersRevealed++;
      this.penalties += 15;

      this._checkActiveWordCompletion();
      this.moveCursorForward();
      return cell.solution;
    }

    /**
     * Reveals the current active word with 50 points penalty
     */
    revealWord() {
      if (!this.activeWord) return null;
      const cells = this.getWordCells(this.activeWord);
      cells.forEach(c => {
        c.userChar = c.solution;
        c.isRevealed = true;
        c.isCorrect = true;
        c.isError = false;
      });

      this.hintsUsed++;
      this.wordsRevealed++;
      this.penalties += 50;

      this.completedWords.add(`${this.activeWord.clueNum}-${this.activeWord.direction}`);
      return this.activeWord.word;
    }

    /**
     * Checks all entered letters and flags errors in red
     */
    checkPuzzle() {
      let errors = 0;
      let filled = 0;
      let correct = 0;

      for (let r = 0; r < this.rows; r++) {
        for (let c = 0; c < this.cols; c++) {
          const cell = this.grid[r][c];
          if (!cell.isBlocked) {
            if (cell.userChar !== '') {
              filled++;
              if (cell.userChar === cell.solution) {
                cell.isCorrect = true;
                cell.isError = false;
                correct++;
              } else {
                cell.isError = true;
                cell.isCorrect = false;
                errors++;
              }
            }
          }
        }
      }

      this.errorsMade += errors;
      return { errors, filled, correct };
    }

    /**
     * Verifies if the entire crossword grid is solved correctly
     */
    isPuzzleSolved() {
      for (let r = 0; r < this.rows; r++) {
        for (let c = 0; c < this.cols; c++) {
          const cell = this.grid[r][c];
          if (!cell.isBlocked) {
            if (cell.userChar !== cell.solution) {
              return false;
            }
          }
        }
      }
      this.completed = true;
      return true;
    }

    /**
     * Calculates final performance score and learning XP earned
     */
    calculateFinalScore() {
      const totalWords = this.puzzle.words.length;
      const solvedWords = this.completedWords.size;
      
      // Base: 100 points per solved word
      const basePoints = solvedWords * 100;
      // Bonus: 25 points for completely unassisted solve
      const unassistedBonus = (this.hintsUsed === 0) ? (solvedWords * 25) : 0;
      // Full completion bonus: 150 points
      const fullBonus = this.completed ? 150 : 0;
      
      let rawScore = basePoints + unassistedBonus + fullBonus - this.penalties;
      if (rawScore < 0) rawScore = 0;

      const elapsedSeconds = Math.max(1, Math.floor((Date.now() - this.startTime) / 1000));
      const accuracy = totalWords > 0 ? Math.round((solvedWords / totalWords) * 100) : 0;

      // Learning XP conversion
      const xpEarned = Math.round(rawScore * 0.75);

      return {
        totalWords,
        solvedWords,
        basePoints,
        unassistedBonus,
        fullBonus,
        penalties: this.penalties,
        finalScore: rawScore,
        xpEarned,
        accuracy,
        elapsedSeconds,
        hintsUsed: this.hintsUsed
      };
    }
  }

  window.CrosswordEngine = CrosswordEngine;
})();

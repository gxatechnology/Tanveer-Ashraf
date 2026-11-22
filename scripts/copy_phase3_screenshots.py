import os
import shutil

sandbox_dir = r"C:\Users\tauqe\.gemini\antigravity\brain\df0b389d-1b0e-4bd1-9b97-02e3b31480df\browser_sandbox\screenshots"
dest_dir = r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\assets\games\images\screenshots"

os.makedirs(dest_dir, exist_ok=True)

mapping = {
    "phase3_01_brain_arena_dashboard.png": "step_109_shot_1_phase3_01_brain_arena_dashboard.png",
    "phase3_02_crossword_selector.png": "step_111_shot_1_phase3_02_crossword_selector.png",
    "phase3_03_crossword_intro.png": "step_115_shot_1_phase3_03_crossword_intro.png",
    "phase3_04_crossword_beginner_gameplay.png": "step_121_shot_1_phase3_04_crossword_beginner_gameplay.png",
    "phase3_05_crossword_advanced_gameplay.png": "step_126_shot_1_phase3_05_crossword_advanced_gameplay.png",
    "phase3_06_crossword_clue_hint.png": "step_136_shot_1_phase3_06_crossword_clue_hint.png",
    "phase3_07_crossword_result.png": "step_150_shot_1_phase3_07_crossword_result.png",
    "phase3_08_codebreaker_dashboard.png": "step_156_shot_1_phase3_08_codebreaker_dashboard.png",
    "phase3_09_scramble_active_gameplay.png": "step_160_shot_1_phase3_09_scramble_active_gameplay.png",
    "phase3_10_scramble_tile_interaction.png": "step_167_shot_1_step_166_shot_1_phase3_10_scramble_tile_interact.png",
    "phase3_11_scramble_correct_definition.png": "step_173_shot_1_step_172_shot_1_phase3_11_scramble_correct_defin.png",
    "phase3_12_scramble_manuscript_mode.png": "step_179_shot_1_step_178_shot_1_phase3_12_scramble_manuscript_mo.png",
    "phase3_13_scramble_final_result.png": "step_193_shot_1_step_192_shot_1_phase3_13_scramble_final_result.png",
    "phase3_14_vocabulary_revision_panel.png": "step_199_shot_1_step_198_shot_1_phase3_14_vocabulary_revision_pa.png",
    "phase3_15_mobile_crossword.png": "step_204_shot_1_phase3_15_mobile_crossword.png",
    "phase3_16_mobile_word_scramble.png": "step_273_shot_1.png"
}

all_ok = True
for target, src_file in mapping.items():
    src_path = os.path.join(sandbox_dir, src_file)
    dst_path = os.path.join(dest_dir, target)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        sz = os.path.getsize(dst_path)
        print(f"SUCCESS: {target} ({sz} bytes) copied from {src_file}")
    else:
        print(f"FAILED: {src_file} does not exist!")
        all_ok = False

if all_ok:
    print("\nALL 16 PHASE 3 SCREENSHOTS COPIED SUCCESSFULLY!")
else:
    print("\nSOME SCREENSHOTS FAILED TO COPY.")

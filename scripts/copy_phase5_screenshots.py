import os
import shutil

sandbox_dir = r"C:\Users\tauqe\.gemini\antigravity\brain\df0b389d-1b0e-4bd1-9b97-02e3b31480df\browser_sandbox\screenshots"
dest_dir = r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\assets\games\images\screenshots"

os.makedirs(dest_dir, exist_ok=True)

targets = [
    "phase5_01_master_dashboard.png",
    "phase5_02_pyq_library.png",
    "phase5_03_bns_library.png",
    "phase5_04_smart_legal_search.png",
    "phase5_05_mock_test_centre.png",
    "phase5_06_active_examination.png",
    "phase5_07_results_and_analytics.png",
    "phase5_08_unified_revision_centre.png",
    "phase5_09_complete_brain_arena.png",
    "phase5_10_memory_match.png",
    "phase5_11_section_sprint.png",
    "phase5_12_legal_detective.png",
    "phase5_13_be_the_judge.png",
    "phase5_14_legal_crossword.png",
    "phase5_15_word_scramble.png",
    "phase5_16_legal_myth_buster.png",
    "phase5_17_road_to_judiciary_map.png",
    "phase5_18_achievement_gallery.png",
    "phase5_19_personalized_learning_plan.png",
    "phase5_20_backup_restore_interface.png",
    "phase5_21_educational_achievement_modal.png",
    "phase5_22_mobile_dashboard.png",
    "phase5_23_mobile_examination.png",
    "phase5_24_mobile_myth_buster.png",
    "phase5_25_mobile_revision.png"
]

all_files = os.listdir(sandbox_dir)

copied = {}
for target in targets:
    base = target.replace(".png", "")
    matches = []
    for f in all_files:
        if base in f:
            fp = os.path.join(sandbox_dir, f)
            matches.append((f, os.path.getmtime(fp), os.path.getsize(fp)))
    if matches:
        # Sort by mtime descending to get the newest capture
        matches.sort(key=lambda x: x[1], reverse=True)
        best_match = matches[0][0]
        src_path = os.path.join(sandbox_dir, best_match)
        dst_path = os.path.join(dest_dir, target)
        shutil.copy2(src_path, dst_path)
        copied[target] = (best_match, os.path.getsize(dst_path))

print(f"Copied {len(copied)} / {len(targets)} targets:")
for t in targets:
    if t in copied:
        print(f"  [OK] {t} ({copied[t][1]} bytes) from {copied[t][0]}")
    else:
        print(f"  [MISSING] {t}")

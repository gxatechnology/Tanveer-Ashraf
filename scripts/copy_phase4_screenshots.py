import os
import shutil
import re

sandbox_dir = r"C:\Users\tauqe\.gemini\antigravity\brain\df0b389d-1b0e-4bd1-9b97-02e3b31480df\browser_sandbox\screenshots"
dest_dir = r"C:\Users\tauqe\Documents\Tanveer_Ashraf_Judicial\assets\games\images\screenshots"

os.makedirs(dest_dir, exist_ok=True)

targets = [
    "phase4_01_brain_arena_all_8_games.png",
    "phase4_02_myth_buster_hero.png",
    "phase4_03_myth_classic_mode.png",
    "phase4_04_myth_scales_tilt_true.png",
    "phase4_05_myth_scales_tilt_false.png",
    "phase4_06_myth_scales_tilt_depends.png",
    "phase4_07_myth_find_error_mode.png",
    "phase4_08_myth_correct_law_mode.png",
    "phase4_09_myth_old_vs_new_mode.png",
    "phase4_10_myth_precedent_challenge.png",
    "phase4_11_myth_confidence_challenge.png",
    "phase4_12_myth_grand_trial_mode.png",
    "phase4_13_myth_feedback_authority.png",
    "phase4_14_myth_completion_summary.png",
    "phase4_15_journey_hero_and_readiness.png",
    "phase4_16_journey_interactive_map.png",
    "phase4_17_journey_map_node_hover.png",
    "phase4_18_journey_daily_plan_widget.png",
    "phase4_19_journey_chapters_deck.png",
    "phase4_20_journey_missions_modal.png",
    "phase4_21_journey_mastery_matrix.png",
    "phase4_22_journey_appointment_decree.png",
    "phase4_23_achievements_gallery_38.png",
    "phase4_24_mobile_myth_buster.png",
    "phase4_25_mobile_judiciary_journey.png"
]

all_files = os.listdir(sandbox_dir)

# Explicit manual fallback overrides
explicit = {
    "phase4_01_brain_arena_all_8_games.png": "step_281_shot_1.png"
}

# Find latest file for each target
copied = {}
for target in targets:
    if target in explicit:
        src_path = os.path.join(sandbox_dir, explicit[target])
        dst_path = os.path.join(dest_dir, target)
        shutil.copy2(src_path, dst_path)
        copied[target] = (explicit[target], os.path.getsize(dst_path))
        continue
    base = target.replace(".png", "")
    matches = []
    for f in all_files:
        if base in f:
            fp = os.path.join(sandbox_dir, f)
            matches.append((f, os.path.getmtime(fp), os.path.getsize(fp)))
    if matches:
        # Sort by mtime descending
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

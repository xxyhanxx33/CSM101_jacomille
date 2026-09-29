
jacomille_patients = {
    "ana": (80, 50, 150, 90, 140, 160, 70),
    "ben": (130, 140, 135, 90, 140, 150, 180),
    "carlo": (90, 100, 95, 90, 140, 80, 140)
}

for jacomillepatient, jacomillereadings in jacomille_patients.items():
    print("Patient:", jacomillepatient)

    jacomille_high_count = 0
    print("Blood Sugar Summary")

    for jacomillereading in jacomillereadings:
        if jacomillereading >= 120:
            jacomillestatus = "High"
            jacomille_high_count += 1
        else:
            jacomillestatus = "Normal"

    jacomille_max = max(jacomillereadings)
    jacomille_min = min(jacomillereadings)
    jacomille_avg = sum(jacomillereadings) / len(jacomillereadings)
    jacomille_diff = jacomille_max - jacomille_min

    print("Number of High Readings:", jacomille_high_count)
    print()
    print(f"Maximum Blood Sugar: {jacomille_max:.0f}")
    print(f"Minimum Blood Sugar: {jacomille_min:.0f}")
    print(f"Average Blood Sugar: {jacomille_avg:.0f}")
    print(f"Difference Blood Sugar: {jacomille_diff}")
    print()


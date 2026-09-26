export interface DoseInput {
  weightKg: number;
  doseMgPerKg: number;
}

function positive(value: number, name: string): number {
  if (!Number.isFinite(value) || value <= 0) {
    throw new RangeError(`${name} must be a positive finite number`);
  }
  return value;
}

export function bmi(weightKg: number, heightM: number): number {
  positive(weightKg, "weightKg");
  positive(heightM, "heightM");
  return weightKg / (heightM * heightM);
}

export function weightBasedDose({ weightKg, doseMgPerKg }: DoseInput): number {
  positive(weightKg, "weightKg");
  positive(doseMgPerKg, "doseMgPerKg");
  return weightKg * doseMgPerKg;
}

export function mapToBmiCategory(value: number): string {
  positive(value, "value");
  if (value < 18.5) return "underweight";
  if (value < 25) return "normal";
  if (value < 30) return "overweight";
  return "obesity";
}

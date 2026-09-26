import { bmi, mapToBmiCategory, weightBasedDose } from "./clinical.js";

const weight = 80;
const height = 1.75;

const calculatedBmi = bmi(weight, height);

console.log(JSON.stringify({
  bmi: Number(calculatedBmi.toFixed(2)),
  category: mapToBmiCategory(calculatedBmi),
  exampleDoseMg: weightBasedDose({ weightKg: weight, doseMgPerKg: 15 })
}));

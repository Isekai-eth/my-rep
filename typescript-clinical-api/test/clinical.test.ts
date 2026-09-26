import test from "node:test";
import assert from "node:assert/strict";
import { bmi, mapToBmiCategory, weightBasedDose } from "../src/clinical.js";

test("calculates BMI", () => {
  assert.ok(Math.abs(bmi(80, 1.75) - 26.1224) < 0.0001);
});

test("maps BMI to a category", () => {
  assert.equal(mapToBmiCategory(26.1), "overweight");
});

test("calculates weight-based dose", () => {
  assert.equal(weightBasedDose({ weightKg: 24, doseMgPerKg: 15 }), 360);
});

test("rejects invalid inputs", () => {
  assert.throws(() => bmi(0, 1.75), RangeError);
  assert.throws(() => weightBasedDose({ weightKg: 24, doseMgPerKg: 0 }), RangeError);
});

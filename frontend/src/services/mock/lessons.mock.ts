import type { LessonContent, LessonSummary } from "@/types";

interface LessonSeed {
  slug: string;
  title: string;
  category: string;
  difficulty: LessonContent["difficulty"];
  duration: number;
  explanationMd: string;
  code: string;
  output: string;
  notes: string[];
}

const PYTHON_LESSON_SEEDS: LessonSeed[] = [
  {
    slug: "variables",
    title: "Variables",
    category: "Fundamentals",
    difficulty: "beginner",
    duration: 8,
    explanationMd:
      "A variable is a name that points to a value stored in memory. Python is dynamically typed, so you never declare a type up front — the interpreter figures it out from the value you assign.",
    code: `name = "Ada"\nage = 28\nis_learning = True\n\nprint(name, age, is_learning)`,
    output: "Ada 28 True",
    notes: [
      "Variable names are case-sensitive and can't start with a digit.",
      "Reassigning a variable to a new type is legal in Python — use it sparingly for clarity.",
    ],
  },
  {
    slug: "data-types",
    title: "Data Types",
    category: "Fundamentals",
    difficulty: "beginner",
    duration: 10,
    explanationMd:
      "Python's built-in types cover numbers (int, float, complex), text (str), booleans, and collections (list, tuple, set, dict). `type()` tells you exactly what you're holding.",
    code: `values = [42, 3.14, "hello", True, None]\nfor v in values:\n    print(v, "->", type(v).__name__)`,
    output: "42 -> int\n3.14 -> float\nhello -> str\nTrue -> bool\nNone -> NoneType",
    notes: ["`None` represents the absence of a value, not zero or an empty string."],
  },
  {
    slug: "operators",
    title: "Operators",
    category: "Fundamentals",
    difficulty: "beginner",
    duration: 9,
    explanationMd:
      "Arithmetic (`+ - * / // % **`), comparison (`== != < >`), logical (`and or not`), and assignment operators (`+= -=`) let you combine and compare values.",
    code: `a, b = 17, 5\nprint(a // b, a % b, a ** 2)`,
    output: "3 2 289",
    notes: ["`//` is floor division — it always rounds down toward negative infinity."],
  },
  {
    slug: "strings",
    title: "Strings",
    category: "Fundamentals",
    difficulty: "beginner",
    duration: 12,
    explanationMd:
      "Strings are immutable sequences of characters. Slicing, f-strings, and built-in methods like `.upper()` and `.split()` cover most day-to-day text work.",
    code: `name = "python"\nprint(f"Hello, {name.title()}!")\nprint(name[:3], name[::-1])`,
    output: "Hello, Python!\npyt nohtyp",
    notes: ["f-strings (`f\"...\"`) are the preferred way to format strings since Python 3.6."],
  },
  {
    slug: "lists",
    title: "Lists",
    category: "Collections",
    difficulty: "beginner",
    duration: 11,
    explanationMd:
      "Lists are ordered, mutable collections. You can append, insert, remove, and slice them, and they can hold mixed types.",
    code: `nums = [3, 1, 4, 1, 5]\nnums.append(9)\nnums.sort()\nprint(nums)`,
    output: "[1, 1, 3, 4, 5, 9]",
    notes: ["List comprehensions (`[x*2 for x in nums]`) are the idiomatic way to transform lists."],
  },
  {
    slug: "tuples",
    title: "Tuples",
    category: "Collections",
    difficulty: "beginner",
    duration: 7,
    explanationMd:
      "Tuples look like lists but are immutable — once created, their contents can't change. Use them for fixed groupings like coordinates.",
    code: `point = (3, 4)\nx, y = point\nprint(x, y)`,
    output: "3 4",
    notes: ["Immutability makes tuples hashable, so they can be used as dictionary keys."],
  },
  {
    slug: "sets",
    title: "Sets",
    category: "Collections",
    difficulty: "intermediate",
    duration: 9,
    explanationMd:
      "Sets are unordered collections of unique elements, optimized for membership tests and set algebra (union, intersection, difference).",
    code: `a = {1, 2, 3}\nb = {2, 3, 4}\nprint(a & b, a | b, a - b)`,
    output: "{2, 3} {1, 2, 3, 4} {1}",
    notes: ["Checking `x in a_set` is O(1) on average — much faster than checking a list."],
  },
  {
    slug: "dictionaries",
    title: "Dictionaries",
    category: "Collections",
    difficulty: "intermediate",
    duration: 12,
    explanationMd:
      "Dictionaries store key-value pairs. Since Python 3.7 they preserve insertion order, and `.get()` lets you look up safely with a default.",
    code: `user = {"name": "Ada", "role": "engineer"}\nprint(user.get("role"))\nprint(user.get("age", "unknown"))`,
    output: "engineer\nunknown",
    notes: ["Keys must be hashable — strings, numbers, and tuples work; lists don't."],
  },
  {
    slug: "if-else",
    title: "If Else",
    category: "Control Flow",
    difficulty: "beginner",
    duration: 8,
    explanationMd:
      "Conditional branching with `if / elif / else` runs different code paths based on boolean expressions. Python uses indentation, not braces, to define blocks.",
    code: `score = 82\nif score >= 90:\n    grade = "A"\nelif score >= 75:\n    grade = "B"\nelse:\n    grade = "C"\nprint(grade)`,
    output: "B",
    notes: ["Truthy/falsy values matter: empty strings, 0, and empty collections are all falsy."],
  },
  {
    slug: "loops",
    title: "Loops",
    category: "Control Flow",
    difficulty: "beginner",
    duration: 10,
    explanationMd:
      "`for` loops iterate over sequences; `while` loops repeat until a condition becomes false. `break` and `continue` give you fine-grained control.",
    code: `total = 0\nfor n in range(1, 6):\n    if n == 4:\n        continue\n    total += n\nprint(total)`,
    output: "11",
    notes: ["`enumerate()` gives you both index and value when looping — avoid manual counters."],
  },
  {
    slug: "functions",
    title: "Functions",
    category: "Control Flow",
    difficulty: "intermediate",
    duration: 13,
    explanationMd:
      "Functions bundle reusable logic. Python supports default arguments, keyword arguments, and `*args` / `**kwargs` for flexible signatures.",
    code: `def greet(name, greeting="Hello"):\n    return f"{greeting}, {name}!"\n\nprint(greet("Ada"))\nprint(greet("Sam", greeting="Hey"))`,
    output: "Hello, Ada!\nHey, Sam!",
    notes: ["Type hints (`def greet(name: str) -> str:`) improve readability and tooling support."],
  },
  {
    slug: "oop",
    title: "OOP",
    category: "Advanced",
    difficulty: "advanced",
    duration: 16,
    explanationMd:
      "Classes bundle state and behavior. `__init__` sets up instance attributes, and inheritance lets subclasses extend or override behavior.",
    code: `class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return f"{self.name} makes a sound."\n\nclass Dog(Animal):\n    def speak(self):\n        return f"{self.name} barks."\n\nprint(Dog("Rex").speak())`,
    output: "Rex barks.",
    notes: ["Favor composition over deep inheritance chains when behavior varies a lot between subclasses."],
  },
  {
    slug: "file-handling",
    title: "File Handling",
    category: "Advanced",
    difficulty: "advanced",
    duration: 11,
    explanationMd:
      "The `with open(...)` context manager handles files safely, automatically closing them even if an error occurs mid-read.",
    code: `with open("notes.txt", "w") as f:\n    f.write("Learning Python!")\n\nwith open("notes.txt") as f:\n    print(f.read())`,
    output: "Learning Python!",
    notes: ["Always prefer `with` over manual `open()`/`close()` — it prevents leaked file handles."],
  },
  {
    slug: "exception-handling",
    title: "Exception Handling",
    category: "Advanced",
    difficulty: "advanced",
    duration: 12,
    explanationMd:
      "`try / except / finally` lets your program recover from errors gracefully instead of crashing outright.",
    code: `try:\n    result = 10 / 0\nexcept ZeroDivisionError as e:\n    print("Caught:", e)\nfinally:\n    print("Done")`,
    output: "Caught: division by zero\nDone",
    notes: ["Catch specific exceptions rather than a bare `except:` so bugs don't get silently swallowed."],
  },
];

export function getMockLessonSummaries(moduleSlug: string): LessonSummary[] {
  if (moduleSlug !== "python") return [];
  return PYTHON_LESSON_SEEDS.map((seed, index) => ({
    id: `python-${seed.slug}`,
    moduleSlug: "python",
    slug: seed.slug,
    title: seed.title,
    category: seed.category,
    order: index + 1,
    durationMinutes: seed.duration,
    difficulty: seed.difficulty,
    isCompleted: index < 4,
    isLocked: index > 7,
  }));
}

export function getMockLessonContent(moduleSlug: string, lessonSlug: string): LessonContent | null {
  if (moduleSlug !== "python") return null;
  const index = PYTHON_LESSON_SEEDS.findIndex((l) => l.slug === lessonSlug);
  if (index === -1) return null;
  const seed = PYTHON_LESSON_SEEDS[index];
  const next = PYTHON_LESSON_SEEDS[index + 1] ?? null;

  return {
    id: `python-${seed.slug}`,
    moduleSlug: "python",
    slug: seed.slug,
    title: seed.title,
    category: seed.category,
    order: index + 1,
    durationMinutes: seed.duration,
    difficulty: seed.difficulty,
    isCompleted: index < 4,
    isLocked: index > 7,
    explanationMd: seed.explanationMd,
    codeExample: { language: "python", code: seed.code },
    output: seed.output,
    notes: seed.notes,
    nextLessonSlug: next?.slug ?? null,
  };
}

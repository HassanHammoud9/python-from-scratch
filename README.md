# Python from Scratch: Learn by Typing, Not by Watching

> I got tired of watching tutorials and still not being able to code. So I built this.

## Why This Exists

Here's something nobody talks about: we're in an era where AI can write code for you. GitHub Copilot autocompletes your functions. ChatGPT generates entire scripts. And that's great, until you realize you can't read what it generated, can't debug it when it breaks, and can't modify it to fit your actual needs.

AI is a tool. But a tool is useless if you don't understand what it's doing.

I started this project because I wanted to actually *understand* Python. Not "watch a 12-hour course and forget it by next week" understand. Actually understand. The kind where your fingers know what to type before your brain finishes the thought.

The method is simple and a bit old school: **type the code yourself, repeatedly, until it sticks.** No copying. No pasting. Just you, a text editor, and repetition until it clicks.

It worked for me. I'm sharing it because I think it can work for others too.

## Who This Is For

- You're learning Python for the first time and want something hands-on
- You've watched tutorials but still freeze when you open an empty file
- You're preparing for coding interviews and need to drill the fundamentals
- You're a developer who uses AI tools daily but wants to strengthen your foundation
- You learn best by doing, not by reading

## What's Inside

This repo is split into two parts. Start with the basics. Move to DSA when you're comfortable.

### Part 1: Python Basics (12 Steps)

Everything from "what is print()" to building small projects. Each step has a tutorial explanation and a practice file you type out yourself.

| Step | Topic | File |
|------|-------|------|
| 1 | Print statements | `basics/step1_practice.py` |
| 2 | Variables | `basics/step2_practice.py` |
| 3 | String concatenation | `basics/step3_practice.py` |
| 4 | Math operations | `basics/step4_practice.py` |
| 5 | User input | `basics/step5_practice.py` |
| 6 | Type conversion | `basics/step6_practice.py` |
| 7 | If statements | `basics/step7_practice.py` |
| 8 | Loops | `basics/step8_practice.py` |
| 9 | Lists | `basics/step9_practice.py` |
| 10 | Functions | `basics/step10_practice.py` |
| 11 | Mini projects | `basics/step11_projects.py` |
| 12 | Common patterns | `basics/step12_patterns.py` |

**Bonus:** `basics/exercises_to_solve.py` has 20 standalone exercises to test yourself.

Full tutorial with explanations: [`PYTHON_TUTORIAL.md`](PYTHON_TUTORIAL.md)

### Part 2: Data Structures & Algorithms (16 Steps)

Once you've got the basics down, this takes you from dictionaries all the way to dynamic programming and trees. Each step includes LeetCode-style problems so you can apply what you learn immediately.

| Step | Topic | File |
|------|-------|------|
| 1 | Dictionaries / Hash Maps | `dsa/dsa_step1_dictionaries.py` |
| 2 | Sets | `dsa/dsa_step2_sets.py` |
| 3 | Tuples | `dsa/dsa_step3_tuples.py` |
| 4 | Advanced list operations | `dsa/dsa_step4_lists.py` |
| 5 | String manipulation | `dsa/dsa_step5_strings.py` |
| 6 | Collections module | `dsa/dsa_step6_collections.py` |
| 7 | Time & space complexity | `dsa/dsa_step7_complexity.py` |
| 8 | Two pointers | `dsa/dsa_step8_two_pointers.py` |
| 9 | Sliding window | `dsa/dsa_step9_sliding_window.py` |
| 10 | Hash map patterns | `dsa/dsa_step10_hashmap_patterns.py` |
| 11 | Sorting & binary search | `dsa/dsa_step11_sorting_searching.py` |
| 12 | Stack & queue | `dsa/dsa_step12_stack_queue.py` |
| 13 | Recursion & backtracking | `dsa/dsa_step13_recursion.py` |
| 14 | Dynamic programming | `dsa/dsa_step14_dynamic_programming.py` |
| 15 | Trees & graphs | `dsa/dsa_step15_trees_graphs.py` |
| 16 | Problem-solving framework | `dsa/dsa_step16_problem_solving.py` |

Full tutorial with explanations: [`DSA_LEETCODE_TUTORIAL.md`](DSA_LEETCODE_TUTORIAL.md)

### Extras

Supplementary reference files for common sticking points:

- `extras/type_conversion_guide.py` - When to use int(), float(), str() and why
- `extras/int_float_mixing.py` - Can you mix ints and floats? (yes, with caveats)
- `extras/print_tips.py` - Different ways to format your print output
- `extras/hello.py` - My very first Python file, bugs and all (kept it real)

## How to Use This

```bash
# Clone the repo
git clone https://github.com/HassanHammoud9/python-from-scratch.git
cd python-from-scratch

# Start with step 1
python3 basics/step1_practice.py
```

The approach:

1. **Read the tutorial** for context on what you're about to learn
2. **Open the practice file** for that step
3. **Type it out yourself.** Don't copy paste. Your fingers need to learn this.
4. **Run it.** See what happens. Break it. Fix it.
5. **Do it again.** 3 to 4 times minimum. Sounds excessive? That's the point. Repetition is how you build instinct.
6. **Move on** only when you can write it without looking at the example

## The Learning Path

```
Week 1-2    Python Basics (Steps 1-12)
            You should be comfortable writing small programs from scratch.

Week 3-4    Data Structures (DSA Steps 1-6)
            Dictionaries, sets, tuples, advanced lists, strings, collections.

Week 5-6    Algorithms (DSA Steps 7-15)
            Two pointers, sliding window, binary search, stacks, recursion, DP, trees.

Week 7+     LeetCode & Interview Prep (DSA Step 16)
            Apply everything. Solve problems. Time yourself. Get uncomfortable.
```

This timeline assumes roughly an hour a day. Go faster or slower based on your schedule. The only wrong pace is zero.

## A Note on "Learning in the Age of AI"

Look, I'm not anti-AI. I use AI tools. They're incredible for productivity. But here's what I've noticed: the developers who get the most out of AI are the ones who already understand the fundamentals.

When Copilot suggests a sliding window solution, you need to know *why* that's the right approach. When ChatGPT generates a recursive function, you need to know if it'll blow your stack on large inputs. When the AI gets it wrong (and it will), you need the skills to catch it and fix it.

This repo exists because the fundamentals aren't going away. If anything, they matter more now. The developers who invest in understanding the "why" behind the code will always have an edge over those who just copy the output.

So yeah. Type it out. Understand it. Make it yours.

## Project Structure

```
python-from-scratch/
├── basics/                        # Python fundamentals (Steps 1-12)
│   ├── step1_practice.py          # Print statements
│   ├── step2_practice.py          # Variables
│   ├── ...                        # Steps 3-10
│   ├── step11_projects.py         # Mini projects (calculator, guessing game, todo list)
│   ├── step12_patterns.py         # Common patterns (validation, counting, max/min)
│   └── exercises_to_solve.py      # 20 exercises to solve on your own
│
├── dsa/                           # Data structures & algorithms (Steps 1-16)
│   ├── dsa_step1_dictionaries.py  # Hash maps
│   ├── dsa_step2_sets.py          # Sets
│   ├── ...                        # Steps 3-15
│   └── dsa_step16_problem_solving.py  # Problem-solving framework
│
├── extras/                        # Reference files and quick guides
│   ├── type_conversion_guide.py
│   ├── int_float_mixing.py
│   ├── print_tips.py
│   └── hello.py                   # My first Python file (bugs included)
│
├── PYTHON_TUTORIAL.md             # Full basics tutorial with explanations
├── DSA_LEETCODE_TUTORIAL.md       # Full DSA tutorial with LeetCode problems
├── DSA_README.md                  # DSA section overview and study plan
├── ROADMAP.md                     # Visual learning roadmap
└── LICENSE                        # MIT License
```

## Contributing

Found a typo? Want to add an exercise? Have a better explanation for something? Open a PR.

This is meant to be a community resource. If it helped you, consider improving it for the next person.

Some ideas for contributions:
- Add solutions to the exercises (in a separate `solutions/` folder)
- Add more practice problems at any level
- Translate the tutorials to other languages
- Add exercises for topics not covered yet (OOP, file I/O, error handling, APIs)
- Fix my terrible first hello.py (or don't, it's a vibe)

## License

MIT. Use it, share it, fork it, teach with it. That's the whole point.

---

*Built by someone who believes the best way to learn to code is to actually write code. No shortcuts.*

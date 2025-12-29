# Strif

**Strif** is an experimental, goal-driven programming language designed for
**AI control, autonomous agents, and explainable reasoning systems**.

Strif is **not** a general-purpose programming language.
It is a **control language** for systems that need:

- Goals
- Time
- Conditions
- Memory
- Explainability

---

## Why Strif?

Most programming languages answer:
> *How do I do this?*

Strif answers:
> **Why should this happen, when, and until what goal is satisfied?**

This makes Strif suitable for:
- AI agent orchestration
- Autonomous systems
- Planning & reasoning loops
- Explainable AI control

---

## Core Concepts

Strif is built on five primitives:

| Concept | Meaning |
|------|--------|
| `intent` | Initial state / memory |
| `when` | Condition based on memory |
| `after`, `every` | Time-based execution |
| `aim` | Goal to satisfy |
| `observe` | Human-readable explanation |

---

## Example (Strif Agent)

```strif
scripture SystemGuardian

intent system unstable
aim system stable

every 2s
flow
    observe system state
end

when system unstable
after 4s
flow
    system stable
end

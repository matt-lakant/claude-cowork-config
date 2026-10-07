---
name: cs-agent-builder
description: "Builds a new customer success routine (agent) for a job Matt keeps doing by hand: asks up to five questions, writes the routine file with trigger, inputs, files it may read and write, steps and a never-does list, and saves it to brain/agents/. Use when Matt says \"build me an agent for...\", \"automate this CS job\", \"make a routine for...\"."
---

# CS 15: Agent Builder

Job: a new routine in the same shape as the seven in `cs-brain`.

## Inputs

The job Matt keeps repeating: what kicks it off, what he looks at, what he produces, who gets
it.

## Work

1. Ask up to five questions (AskUserQuestion) to pin down the trigger, the inputs, the output
   and the limits.
2. Write the routine file: name, one-line description, when it runs, which brain files it
   reads, which it may write to, the steps, and what it must never do.
3. List the existing cs- skills it should call rather than redo.

## Output

A finished routine file saved to `brain/agents/<name>.md` after go, plus a three-case test: a
normal day, an empty day and a messy one. `cs-brain` runs routines from that folder by name.

Every routine gets a never-does list. At minimum: never contacts a customer, never deletes a
file, never invents data.

To make a routine part of the plugin itself, it goes into `cs-brain` through `config-sync`, not
into the repo from here.

## When not to use it

Matt has done the job twice. Do it by hand five times first, so the routine reflects what the
job really involves.

## Brain rules (reference copy in `cs-brain`)

- Locate the brain first (`cs-brain` > Where the brain lives). If a file this skill needs is
  missing or empty, say so and stop. Do not work around it.
- File only what the sources say. Anything inferred is labelled INFERRED and stays out of the
  brain until Matt confirms it.
- Renewal date, seat count, plan and contract value come from a source or stay UNKNOWN.
- Show the change list first and write only after Matt says go. Add lines, never overwrite;
  flag conflicts. Archive, never delete.
- Every claim carries the file and date it came from. Dates are `YYYY-MM-DD`.
- Never contact a customer and never send anything. Draft; Matt sends.

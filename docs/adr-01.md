# ADR 01: Use Guardrails for Prompt Moderation

## Status
Proposed

## Context
Enterprise LLM deployments require safety, schema enforcement, and moderation to ensure reliable and compliant outputs.

## Decision
We will use `guardrails-ai` as the primary moderation framework, with custom rules as needed.

## Consequences
- ✅ Provides structured moderation, easily extended
- ⚠️ Adds small latency overhead
- ✅ Aligns with enterprise Responsible AI standards

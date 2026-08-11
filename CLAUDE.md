# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A **fork of Quartz v4** used as one person's digital garden, published to GitHub Pages at `yuricoppe.github.io`. Two very different kinds of work happen here:

- **Content work** — editing `content/`, an Obsidian vault of pt-BR notes on UX/UI design, accessibility, and design systems. This is the majority of the work.
- **Engine work** — `quartz/`, `quartz.config.ts`, `quartz.layout.ts`. `quartz/` is upstream Quartz source; prefer configuring over patching it, since local edits there conflict on upstream merges.

`README.md` and `package.json` are upstream Quartz's and describe the generator, not this site. For this site's actual context, read `openspec/project.md`.

## Commands

```bash
npx quartz build              # build content/ -> public/
npx quartz build --serve      # local dev server with hot reload
npm run check                 # tsc --noEmit + prettier --check
npm run format                # prettier --write
npm test                      # tsx --test (only quartz/util/{path,fileTrie}.test.ts exist)
npx tsx --test quartz/util/path.test.ts   # single test file
npm run docs                  # serve docs/ as a Quartz site
node scripts/format-content.mjs --dry-run # preview content normalization (also: --test)
```

`scripts/format-content.mjs` is a local one-off written for a Notion import: it normalizes whitespace, converts `![[image.png]]` embeds, adds missing frontmatter, and rewrites body `#` to `##`. It rewrites every file under `content/` with no confirmation — always `--dry-run` first.

## CI does not run in this fork

`.github/workflows/ci.yaml` is gated on `if: github.repository == 'jackyzha0/quartz'`, so type checks and tests **never run here**. Only `deploy.yml` runs: a push to `v4` builds and publishes to GitHub Pages.

`v4` is both the default branch and the production branch — pushing to it deploys. Verify changes locally with `npx quartz build` (and `npm run check` for engine edits) before pushing.

## Link resolution — the main content gotcha

`quartz.config.ts` sets `Plugin.CrawlLinks({ markdownLinkResolution: "shortest" })`. Per `transformLink` in `quartz/util/path.ts`, that means:

- A **bare filename** with no slash resolves if it is unique across the vault: `[[persona]]` ✅
- **Anything containing a slash** is resolved as an absolute path from the vault root, which is `content/` — _not_ from the current file's folder.

So folder-relative wikilinks silently break. From `content/Glossário/Componentes/messaging.md`:

```
[[Componentes/toast]]              ❌ resolves to /Componentes/toast
[[../index]]                       ❌ ".." is not supported
[[Glossário/Componentes/toast]]    ✅ absolute from content/
```

There is **no build error** for a broken wikilink — the build succeeds and the link is dead on the site. When touching links, verify by resolving every target against the file list rather than trusting the build.

**Never rely on `aliases:` for wikilink resolution — link with the full path from `content/`.** Aliases reliably produce redirect pages at build time, but their participation in link resolution is unreliable, and it fails in both directions:

- `transformLink` (`quartz/util/path.ts`) only takes the bare-filename shortcut when exactly _one_ slug ends with that name. `FrontMatter` pushes alias slugs into `ctx.allSlugs` during parsing, so an alias ending in the same segment as a page's own filename can shadow it — two matches, shortcut skipped, link falls back to an absolute path from the vault root that does not exist. This bit `content/UX Healthcare/UX Login e Cadastro.md` and its Notion-derived alias `UX Healthcare/UX Login e Cadastro/UX Login e Cadastro` (confirmed by removing the alias and rebuilding).
- The reverse also fails: an alias covering a page's _old_ name does not necessarily make `[[Old Name]]` resolve, because `ctx.allSlugs` is mutated during parsing and reset in `build.ts` afterwards, so what a given file sees depends on processing order. This bit `content/Pagamento/index.md`, still linking a page by the title it had before being renamed.

Keep the aliases — they preserve published URLs — but write links as `[[Folder/File|Label]]`.

Related: Quartz has no `README.md` convention, so a folder's landing page must be `index.md`. `FolderPage`/`TagPage` emitters generate folder and tag listings automatically, so a folder `index.md` is optional.

## Fork do layout: o que foi tocado em `quartz/`

O layout de três colunas no estilo GitHub Docs vive quase todo em pontos de
extensão que não conflitam com o upstream:

- `quartz/styles/custom.scss` — existe para isso e concentra a grade, as barras
  fixas, o recolher da esquerda e a gaveta responsiva
- `quartz.layout.ts` — configuração, não é código do upstream
- `quartz/components/TopBar.tsx`, `ContextBar.tsx`, `styles/topbar.scss`,
  `styles/contextbar.scss`, `scripts/sidebar.inline.ts` — arquivos novos

**A única edição em arquivo do upstream é `quartz/components/index.ts`**: dois
imports e duas entradas no `export`. Num merge com o upstream, é o único ponto de
conflito esperado, e a resolução é reaplicar as quatro linhas.

Componentes que recebem outros componentes precisam recebê-los **por opção**, e
não por `children` — só o `header[]` recebe filhos do `renderPage`. Ver o padrão
em `Flex.tsx`, que `TopBar` e `ContextBar` seguem.

A proposta, as decisões e a auditoria do `index.md` estão em
`openspec/changes/adopt-docs-style-layout/`.

## Content conventions

Defined in `docs/content-authoring-guide.md` (a local addition; the rest of `docs/` is upstream Quartz documentation):

- Frontmatter `title` is required. `description`, `tags`, and `draft` are optional.
- **Body headings start at `##`.** Quartz renders the frontmatter `title` as the h1, so a body `#` produces two h1s.
- `draft: true` excludes a page from the build via the `RemoveDrafts` filter.
- Images live in `content/attachments/`.
- `ignorePatterns` in `quartz.config.ts` skips `private`, `templates`, and `.obsidian`.

Keep Obsidian compatibility in mind: content is authored in Obsidian and arrives through bulk automated commits titled `Quartz sync: <date>`. Wikilinks and `![[embeds]]` must stay valid in both Obsidian and Quartz.

**Do not mass-apply link markup with regex over `content/`.** A past automated auto-linking pass linked every occurrence of common words ("cor", "link", "ícone") throughout `content/Glossário/`, which produced malformed nested wikilinks (`[[[...]]`), links injected into fenced code blocks and HTML tag names, links inside heading text (corrupting anchors and the table of contents), and thousands of redundant repeats. Cleaning it up touched 132 files. Link the first meaningful mention per page and leave code, headings, and bracketed `[placeholder]` text alone.

## OpenSpec

`AGENTS.md` requires reading `openspec/AGENTS.md` before work that involves a proposal, spec, or plan, or that introduces new capabilities or architecture shifts. Bug fixes, typos, formatting, and config changes are explicitly exempt.

The `openspec` CLI referenced throughout those instructions is **not installed** in this environment, so its `openspec list` / `openspec validate` steps cannot be run as written. `openspec/specs/` is empty; `openspec/changes/standardize-notion-content-formatting/` has all 43 tasks complete but has not been archived.

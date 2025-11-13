# Content Authoring Guide

This guide explains the markdown formatting standards for content files in this Quartz-powered site.

## Frontmatter Metadata

Every markdown file **must** start with YAML frontmatter containing at minimum a `title` field.

### Basic Example

```yaml
---
title: "Page Title"
---
```

### Full Example with Optional Fields

```yaml
---
title: "Page Title"
description: "Brief description for SEO and previews"
tags:
  - ux-design
  - accessibility
draft: false
---
```

### Frontmatter Fields

- **title** (required): Page title shown in navigation and browser tab
- **description** (optional): Brief summary for SEO and link previews
- **tags** (optional): List of topics for categorization
- **draft** (optional): Set to `true` to exclude page from build

## Heading Hierarchy

Use proper heading hierarchy starting with h2 (`##`) for main sections. Quartz automatically uses the frontmatter title as the h1 heading.

### ✅ Correct

```markdown
---
title: "Page Title"
---

## Main Section

Content here...

### Subsection

More content...

#### Sub-subsection

Details...
```

### ❌ Incorrect

```markdown
---
title: "Page Title"
---

# Main Section  ← Don't use h1 in content body

Content...
```

## Whitespace and Formatting

### Section Separation

Use **exactly one blank line** between sections:

```markdown
## Section One

Content here.

## Section Two

More content.
```

### Horizontal Rules

Use horizontal rules (`---`) sparingly to separate major content areas:

```markdown
## Links Section

[Link 1](https://example.com)
[Link 2](https://example.com)

---

## Notes Section

Additional notes...
```

### End of File

Files should end with a single newline character, no trailing whitespace.

## Images

### Standard Markdown Format

Use standard markdown image syntax with proper relative paths:

```markdown
![Alt text description](../attachments/image-name.png)
```

### Image Organization

- Store all images in `content/attachments/` directory
- Use descriptive alt text for accessibility
- URL-encode filenames with spaces: `image%20name.png`

### Example

```markdown
![Diagram showing user flow](attachments/user-flow-diagram.png)
```

## Links

### External Links

Format external links on a single line:

```markdown
[Link Text](https://example.com)
```

### Internal Links (Wikilinks)

Use double-bracket wikilink format for internal pages:

```markdown
[[Page Name]]
[[folder/Page Name]]
```

### Link Lists

When creating lists of links, place each on its own line:

```markdown
## Resources

[Resource 1](https://example.com/1)
[Resource 2](https://example.com/2)
[Resource 3](https://example.com/3)
```

## Lists

### Unordered Lists

Use `-` or `*` with a space:

```markdown
- Item one
- Item two
  - Nested item
  - Another nested item
- Item three
```

### Ordered Lists

Use `1.` format with a space:

```markdown
1. First step
2. Second step
   - Sub-item
   - Another sub-item
3. Third step
```

## Callout Blocks

Quartz supports Obsidian-style callouts for emphasis:

### Basic Callout

```markdown
> [!info] Title
> Content goes here.
```

### Callout Types

- `[!info]` - Information
- `[!note]` - Note
- `[!tip]` - Tip or suggestion
- `[!warning]` - Warning or caution

### Multi-paragraph Callout

```markdown
> [!tip] Pro Tip
> First paragraph.
>
> Second paragraph.
```

## Complete Example

Here's a complete example combining all formatting guidelines:

```markdown
---
title: "UX Design Principles"
description: "Core principles for effective user experience design"
tags:
  - ux-design
  - design-principles
---

## Introduction

This page covers fundamental UX design principles.

## Core Principles

### User-Centered Design

User-centered design focuses on:

- Understanding user needs
- Iterative design process
- Continuous testing and feedback

### Visual Hierarchy

![Visual hierarchy example](attachments/visual-hierarchy.png)

> [!tip] Best Practice
> Always test your designs with real users.

## Resources

[[Design System]]
[[UI Design]]

[Nielsen Norman Group](https://www.nngroup.com/)
[UX Design.cc](https://uxdesign.cc/)

---

## Further Reading

Additional resources and case studies...
```

## Tips for Content Authors

1. **Preview your changes** - Build locally with `npx quartz build` before committing
2. **Use descriptive titles** - Help users and search engines understand your content
3. **Add descriptions** - Especially for index pages and key topics
4. **Maintain consistency** - Follow the same formatting patterns across all pages
5. **Check wikilinks** - Ensure internal links point to existing pages
6. **Optimize images** - Compress images before adding to keep site fast
7. **Write alt text** - Make images accessible to all users

## Running the Formatter

An automated formatting script is available to standardize content:

```bash
# Dry run (see what would change)
node scripts/format-content.mjs --dry-run

# Process all files
node scripts/format-content.mjs

# Test on sample files
node scripts/format-content.mjs --test
```

The script will:

- Add missing frontmatter
- Fix heading hierarchy
- Convert Notion-style image embeds
- Normalize whitespace
- Standardize horizontal rules

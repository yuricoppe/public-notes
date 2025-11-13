#!/usr/bin/env node

/**
 * Content Formatting Script
 * Standardizes Notion-exported markdown files for Quartz v4
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/**
 * Normalize whitespace in markdown content
 * - Remove excessive blank lines (max 2 consecutive)
 * - Ensure single blank line between sections
 * - Remove trailing whitespace
 */
function normalizeWhitespace(content) {
  // Remove trailing whitespace from each line
  content = content.split('\n').map(line => line.trimEnd()).join('\n');
  
  // Replace 3+ consecutive blank lines with 2
  content = content.replace(/\n\n\n+/g, '\n\n');
  
  // Ensure single blank line before headings (except first line)
  content = content.replace(/([^\n])\n(#{2,})/g, '$1\n\n$2');
  
  // Ensure single blank line after headings
  content = content.replace(/(#{2,}[^\n]+)\n([^\n#])/g, '$1\n\n$2');
  
  // Ensure file ends with single newline
  content = content.trimEnd() + '\n';
  
  return content;
}

/**
 * Convert Notion-style image embeds to standard markdown
 * ![[Pasted image 20251105224911.png]] -> ![Image](../attachments/Pasted%20image%2020251105224911.png)
 */
function convertImageEmbeds(content, filePath) {
  const imageRegex = /!\[\[([^\]]+\.(png|jpg|jpeg|gif|svg|webp))\]\]/gi;
  
  return content.replace(imageRegex, (match, filename) => {
    // URL-encode the filename
    const encodedFilename = encodeURIComponent(filename).replace(/%2F/g, '/');
    
    // Determine relative path to attachments based on file depth
    const rootDir = path.resolve(__dirname, '..');
    const contentDir = path.join(rootDir, 'content');
    const fileDir = path.dirname(filePath);
    const relPath = path.relative(fileDir, contentDir);
    
    // Build path to attachments
    let relativePath;
    if (relPath === '') {
      relativePath = 'attachments/';
    } else {
      relativePath = relPath + '/attachments/';
    }
    
    // Extract a simple description from filename
    const description = filename.replace(/^Pasted image \d+\./, '').replace(/\.\w+$/, '') || 'Image';
    
    return `![${description}](${relativePath}${encodedFilename})`;
  });
}

/**
 * Add frontmatter if missing
 * Derives title from filename
 */
function ensureFrontmatter(content, filename) {
  // Check if frontmatter already exists
  if (content.trim().startsWith('---')) {
    return content;
  }
  
  // Derive title from filename
  const title = filename
    .replace(/\.md$/, '')
    .replace(/^index$/, 'Index')
    .replace(/_/g, ' ')
    .trim();
  
  const frontmatter = `---
title: "${title}"
---

`;
  
  return frontmatter + content;
}

/**
 * Fix heading hierarchy
 * Convert h1 (#) to h2 (##) in content body, but preserve frontmatter
 */
function fixHeadingHierarchy(content) {
  const lines = content.split('\n');
  let inFrontmatter = false;
  let frontmatterEnded = false;
  let frontmatterCount = 0;
  
  const fixedLines = lines.map((line, index) => {
    // Track frontmatter boundaries
    if (line.trim() === '---') {
      frontmatterCount++;
      if (frontmatterCount === 1) {
        inFrontmatter = true;
      } else if (frontmatterCount === 2) {
        inFrontmatter = false;
        frontmatterEnded = true;
      }
      return line;
    }
    
    // Skip lines in frontmatter
    if (inFrontmatter) {
      return line;
    }
    
    // Convert h1 to h2 in content body (after frontmatter or if no frontmatter)
    if ((frontmatterEnded || frontmatterCount === 0) && line.match(/^# [^#]/)) {
      return '#' + line;
    }
    
    return line;
  });
  
  return fixedLines.join('\n');
}

/**
 * Normalize horizontal rule usage
 * Ensure proper spacing around horizontal rules
 */
function normalizeHorizontalRules(content) {
  // Ensure blank line before and after horizontal rules
  content = content.replace(/([^\n])\n---\n/g, '$1\n\n---\n\n');
  content = content.replace(/\n---\n([^\n])/g, '\n\n---\n\n$1');
  
  // Clean up excessive spacing
  content = content.replace(/\n\n\n+---/g, '\n\n---');
  content = content.replace(/---\n\n\n+/g, '---\n\n');
  
  return content;
}

/**
 * Process a single markdown file
 */
function processFile(filePath, options = {}) {
  const { dryRun = false } = options;
  
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const filename = path.basename(filePath);
    
    let processed = content;
    
    // Apply transformations
    processed = ensureFrontmatter(processed, filename);
    processed = fixHeadingHierarchy(processed);
    processed = convertImageEmbeds(processed, filePath);
    processed = normalizeWhitespace(processed);
    processed = normalizeHorizontalRules(processed);
    
    // Check if changes were made
    if (processed !== content) {
      if (!dryRun) {
        fs.writeFileSync(filePath, processed, 'utf-8');
        console.log(`✓ Processed: ${filePath}`);
      } else {
        console.log(`Would process: ${filePath}`);
      }
      return true;
    } else {
      if (options.verbose) {
        console.log(`  No changes needed: ${filePath}`);
      }
    }
    
    return false;
  } catch (error) {
    console.error(`✗ Error processing ${filePath}:`, error.message);
    return false;
  }
}

/**
 * Process all markdown files in a directory recursively
 */
function processDirectory(dirPath, options = {}) {
  const files = fs.readdirSync(dirPath);
  let processedCount = 0;
  
  for (const file of files) {
    const filePath = path.join(dirPath, file);
    const stat = fs.statSync(filePath);
    
    if (stat.isDirectory()) {
      processedCount += processDirectory(filePath, options);
    } else if (file.endsWith('.md')) {
      if (processFile(filePath, options)) {
        processedCount++;
      }
    }
  }
  
  return processedCount;
}

// Main execution
const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const testMode = args.includes('--test');

const rootDir = path.resolve(__dirname, '..');
const contentDir = path.join(rootDir, 'content');

console.log('Content Formatting Script');
console.log('========================\n');

if (dryRun) {
  console.log('DRY RUN MODE - No files will be modified\n');
}

if (testMode) {
  // Test on a few sample files
  console.log('TEST MODE - Processing sample files\n');
  const testFiles = [
    'content/Gen UI.md',
    'content/index.md',
    'content/Busca/index.md'
  ].map(f => path.join(rootDir, f));
  
  let count = 0;
  for (const file of testFiles) {
    if (fs.existsSync(file)) {
      console.log(`Checking: ${file}`);
      if (processFile(file, { dryRun, verbose: true })) {
        count++;
      }
    } else {
      console.log(`File not found: ${file}`);
    }
  }
  
  console.log(`\n${count} test file(s) ${dryRun ? 'would be' : 'were'} modified`);
} else {
  // Process all files
  const count = processDirectory(contentDir, { dryRun });
  console.log(`\n${count} file(s) ${dryRun ? 'would be' : 'were'} modified`);
}

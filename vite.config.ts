import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import path from "path";

import { cloudflare } from "@cloudflare/vite-plugin";

// https://vite.dev/config/
export default defineConfig({
  plugins: [tailwindcss(), svelte(), cloudflare()],
  resolve: {
    alias: {
      $lib: path.resolve("./src/lib"),
    },
  },
  base: "/"
});
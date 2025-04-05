import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
	preprocess: vitePreprocess(),
	kit: {
		adapter: adapter({
			pages: 'frontend/build',
			assets: 'frontend/build',
			fallback: 'index.html' // <- wichtig für SPA!
		})
	}
};

export default config;
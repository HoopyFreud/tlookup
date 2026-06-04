<script lang="ts">
	import { Command as CommandPrimitive } from "bits-ui";
	import { cn } from "$lib/utils.js";
    import { Button } from "$lib/components/ui/button/index.js";
	import * as InputGroup from "$lib/components/ui/input-group/index.js";
	import SearchIcon from '@lucide/svelte/icons/search';
	import Shuffle from '@lucide/svelte/icons/shuffle';
	import X from '@lucide/svelte/icons/x';

	let {
		shuffleClickEvent,
		cancelClickEvent,
		ref = $bindable(null),
		class: className,
		value = $bindable(),
		...restProps
	}: CommandPrimitive.InputProps & {
		shuffleClickEvent: Function
		cancelClickEvent: Function
	} = $props();

	if (value === null) {
		value = "";
	}

	export function resetInput() {
		value = "";
		cancelClickEvent();
	}

	export function shuffleInput() {
		shuffleClickEvent();
	}
</script>

<div data-slot="command-input-wrapper" class="p-1 pb-0">
	<InputGroup.Root class="bg-input/30 border-input/30 h-8! rounded-lg! shadow-none! *:data-[slot=input-group-addon]:pl-2!">
		<CommandPrimitive.Input
			{value}
			data-slot="command-input"
			class={cn(
				"w-full text-sm outline-hidden disabled:cursor-not-allowed disabled:opacity-50",
				className
			)}
			{...restProps}
		>
			{#snippet child({ props })}
				<InputGroup.Input {...props} bind:value bind:ref />
			{/snippet}
		</CommandPrimitive.Input>
		<InputGroup.Addon>
			<SearchIcon class="size-4 shrink-0 opacity-50" />
		</InputGroup.Addon>
		<InputGroup.Addon class="gap-0" align="inline-end">
			<Button size="icon-sm" variant="ghost" onclick={()=>shuffleInput()}><Shuffle /></Button>
			<Button size="icon-sm" variant="ghost" onclick={()=>resetInput()}><X /></Button>
		</InputGroup.Addon>
	</InputGroup.Root>
</div>

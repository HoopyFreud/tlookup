<script lang="ts">
	import { Command as CommandPrimitive } from "bits-ui";
	import { cn } from "$lib/utils.js";
	import CheckIcon from '@lucide/svelte/icons/check';

	let {
		isSelected,
		ref = $bindable(null),
		class: className,
		children,
		...restProps
	}: CommandPrimitive.ItemProps & {
		isSelected: boolean;
	} = $props();

	const selectedClass = "bg-muted text-foreground *:[svg]:text-foreground"
	const classString = "group/command-item relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-hidden select-none in-data-[slot=dialog-content]:rounded-lg! data-[disabled=true]:pointer-events-none data-[disabled=true]:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
	const classStringWithSelection = $derived(isSelected?cn(classString,selectedClass):classString);
</script>

<CommandPrimitive.Item
	bind:ref
	data-slot="command-item"
	class={cn(classStringWithSelection,className)}
	{...restProps}
>
	{@render children?.()}
	<CheckIcon class="cn-command-item-indicator ml-auto opacity-0 group-has-data-[slot=command-shortcut]/command-item:hidden group-data-[checked=true]/command-item:opacity-100" />
</CommandPrimitive.Item>

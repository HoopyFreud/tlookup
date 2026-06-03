<script lang="ts">
	import { cn } from "$lib/utils.js";
	import { Command as CommandPrimitive } from "bits-ui";

	export type CommandRootApi = CommandPrimitive.Root;

	let {
		api = $bindable(null),
		ref = $bindable(null),
		value = "",
		class: className,
		...restProps
	}: CommandPrimitive.RootProps & {
		api?: CommandRootApi | null;
	} = $props();
</script>

<CommandPrimitive.Root
	bind:this={api}
	bind:value
	bind:ref
	data-slot="command"
	class={cn("bg-popover text-popover-foreground rounded-xl! p-1 flex w-full h-1/3 flex-col overflow-hidden", className)}
	{...restProps}
/>

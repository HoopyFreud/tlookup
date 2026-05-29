<script>
	import './app.css';
  	import * as Command from "$lib/components/ui/command-scrollbar/index.js";
    import Button from '$lib/components/ui/button/button.svelte';

	const cardGroups = [
	{
		value: "coins",
		label: "Coins",
		cards: [
		{
			value: "1C",
			label: "Ace of Coins"
		},
		{
			value: "2C",
			label: "2 of Coins"
		},
		{
			value: "3C",
			label: "3 of Coins"
		}
		]
	},
	{
		value: "wands",
		label: "Wands",
		cards: [
		{
			value: "1W",
			label: "Ace of Wands"
		},
		{
			value: "2W",
			label: "2 of Wands"
		},
		{
			value: "3W",
			label: "3 of Wands"
		}
		]
	}
  ];

  const flatCards = cardGroups.flatMap((suit) => suit.cards);

  let selectValue = $state("");
  let inputLabel = $derived(flatCards.find((f) => f.value == selectValue)?.label);
  let selectLabel = $derived(flatCards.find((f) => f.value == selectValue)?.label);
</script>
 
<Command.Root class="rounded-lg border shadow-md md:min-w-[450px]" value={selectValue}>
 <Command.Input placeholder="Select or search for a card" bind:value={inputLabel}/>
 <Command.List class="overflow-y-auto h-40">
  <Command.Empty>No cards found</Command.Empty>
  {#each cardGroups as suit}
  	<Command.Group heading={suit.label}>
	  {#each suit.cards as card}
   		<Command.Item aria-selected={card.value === selectValue?true:false}
		onSelect={() => {
		  selectValue = card.value;
		}}>
    	  <span>{card.label}</span>
   		</Command.Item>
	  {/each}
  	</Command.Group>
    <Command.Separator />
  {/each}
 </Command.List>
</Command.Root>

<Button variant="outline">Add to Tableau</Button>

<span>{selectLabel}</span>
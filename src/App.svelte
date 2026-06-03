<script lang="ts">
	import './app.css';
  	import * as Command from "$lib/components/ui/command-scrollbar/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
    import { Button, buttonVariants } from "$lib/components/ui/button/index.js";

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

  let cardTableauArray: Array<{ value: string, label: string }> = $state([])

  let selectValue = $state("");
  let inputLabel = $derived(flatCards.find((f) => f.value == selectValue)?.label);

  let inputComponent:Command.Input;

  function resetSelectValue() {
	selectValue = "";
  }
  
  function addToTableuClick() {
	if(selectValue) {
	  const newTableauCard = flatCards.find((f) => f.value == selectValue)
	  if (newTableauCard) {
	    cardTableauArray.push(newTableauCard);
	    inputComponent.resetInput();
	    resetSelectValue()
	  }
	}
  }

  function removeFromTableuClick(cardIndex:number) {
	cardTableauArray.splice(cardIndex,1)
  }
</script>

<div class="h-3/4 overflow-y-auto">
{#each cardTableauArray as tableauCard, tableauCardIndex}
  <Card.Root class="w-full max-w-xs">
    <Card.Header>
	  <Card.Title>{tableauCard.label}</Card.Title>
 	</Card.Header>
    <Card.Content>
	  <p>Card Content</p>
 	</Card.Content>
 	<Card.Footer class="place-content-center">
	  <Button variant="destructive" onclick={()=>removeFromTableuClick(tableauCardIndex)} >Remove</Button>
 	</Card.Footer>
  </Card.Root>
{/each}
</div>
<span>{selectValue}</span>

<Command.Root class="rounded-lg border shadow-md md:min-w-[450px]" value={selectValue} disablePointerSelection={true} vimBindings={false}>
 <Command.Input placeholder="Select or search for a card" cancelClickEvent={resetSelectValue} bind:value={inputLabel} bind:this={inputComponent}/>
 <Command.List class="overflow-y-auto">
  <Command.Empty>No cards found</Command.Empty>
  {#each cardGroups as suit}
  	<Command.Group heading={suit.label}>
	  {#each suit.cards as card}
   		<Command.Item isSelected={selectValue == card.value} onSelect={() => {selectValue = card.value;}}>
    	  <span>{card.label}</span>
   		</Command.Item>
	  {/each}
  	</Command.Group>
    <Command.Separator />
  {/each}
 </Command.List>
</Command.Root>

<Button variant="secondary" disabled={!selectValue} onclick={()=>addToTableuClick()} >Add to Tableau</Button>
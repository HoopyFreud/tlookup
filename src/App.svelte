<script lang="ts">
  import './app.css';
  import * as Command from "$lib/components/ui/command-scrollbar/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
  import { Separator } from "$lib/components/ui/separator/index.js";

  import cardTable from "./assets/cardTable.json";

  const suitedCards = 
  [
	{
	  name: "Major Arcana",
	  cards: cardTable.filter((card) => card.id.charAt(0)=="M")
	},
	{
	  name: "Coins",
	  cards: cardTable.filter((card) => card.id.charAt(0)=="C")
	},
	{
	  name: "Cups",
	  cards: cardTable.filter((card) => card.id.charAt(0)=="U")
	},
	{
	  name: "Wands",
	  cards: cardTable.filter((card) => card.id.charAt(0)=="W")
	},
	{
	  name: "Swords",
	  cards: cardTable.filter((card) => card.id.charAt(0)=="S")
	}
  ]

  let cardTableauArray: Array<{ name: string, id: string, keyword: string, text: Array<string>}> = $state([])

  let selectID = $state("");
  let selectCard = $derived(cardTable.find((f) => f.id == selectID));

  let inputComponent:Command.Input;

  function resetSelectID() {
	selectID = "";
  }
  
  function addToTableuClick() {
	if(selectID) {
	  const newTableauCard = cardTable.find((f) => f.id == selectID)
	  if (newTableauCard) {
	    cardTableauArray.push(newTableauCard);
	    inputComponent.resetInput();
	    resetSelectID()
	  }
	}
  }

  function removeFromTableuClick(cardIndex:number) {
	cardTableauArray.splice(cardIndex,1)
  }
</script>

  <div id="app" class="h-dvh">
	<div class="h-1/2">
	  <!-- card selection area -->
	  <Command.Root class={["max-h-full min-h-1/3 rounded-lg border shadow-md md:min-w-112.5",selectID?"h-1/3":"h-full"]} value={selectID} disablePointerSelection={true} vimBindings={false}>
	  <Command.Input placeholder="Select or search for a card" cancelClickEvent={resetSelectID} value={selectCard?.name} bind:this={inputComponent}/>
	  <Command.List class="overflow-y-auto h-full">
	  <Command.Empty>No cards found</Command.Empty>
	  {#each suitedCards as suit}
	  	  <Command.Group heading={suit.name}>
		  {#each suit.cards as card}
			  <Command.Item isSelected={selectID == card.id} onSelect={() => {selectID = card.id;}}>
			  <span>{card.name} - {card.keyword}</span>
			  </Command.Item>
		  {/each}
		  </Command.Group>
		  <Command.Separator />
	  {/each}
	  </Command.List>
	  </Command.Root>
	
	  <!-- selected card display area -->
	  <div class={["max-h-2/3 overflow-y-auto",selectID?"h-2/3":"h-0"]}>
	  {#if selectCard}
	  <Card.Root class="overflow-y-auto max-w-full gap-0 h-full">
		  <Card.Header>
		  <Card.Title>{selectCard.name}</Card.Title>
		  <Card.Description>{selectCard.keyword}</Card.Description>
		  </Card.Header>
		  <Card.Content>
		  {#each selectCard.text as textLine, lineIndex}
			<Separator class="my-4" />
		    <p>
			  {#if lineIndex == 1}
				<b>Inverse:</b>
			  {/if}
			  {textLine}</p>
		  {/each}
		  </Card.Content>
	  </Card.Root>
	  {/if}
	  </div>
	</div>
	<Button class="my-2" variant="secondary" disabled={!selectID} onclick={()=>addToTableuClick()} >Add to Tableau</Button>

	<!-- tableau area -->
	<div class="h-fit overflow-y-auto px-4 gap-4 grid justify-items-center grid-cols-1 md:grid-cols-3 md:min-w-112.5">
	{#each cardTableauArray as tableauCard, tableauCardIndex}
	<Card.Root class="w-full gap-4 min-h-50">
	  <Card.Header>
		<Card.Title>{tableauCard.name}</Card.Title>
		<Card.Description>{tableauCard.keyword}</Card.Description>
	  </Card.Header>
	  <Card.Content>
		<Popover.Root>
  		  <Popover.Trigger class={buttonVariants({ variant: "default" })}>Description</Popover.Trigger>
  		  <Popover.Content class="max-h-[75vh]">
			<Card.Root class="overflow-y-auto w-full gap-4 min-h-50">
	  		  <Card.Header>
				<Card.Title>{tableauCard.name}</Card.Title>
				<Card.Description>{tableauCard.keyword}</Card.Description>
	  		  </Card.Header>
		      <Card.Content>
		        {#each tableauCard.text as textLine, lineIndex}
				  <Separator class="my-4" />
		    	  <p>
					{#if lineIndex == 1}
					  <b>Inverse:</b>
					{/if}
					{textLine}</p>
		  		{/each}
		  	  </Card.Content>
	  		</Card.Root>
		  </Popover.Content>
		</Popover.Root>
	  </Card.Content>
	  <Card.Footer class="place-content-center">
		<Button variant="destructive" onclick={()=>removeFromTableuClick(tableauCardIndex)} >Remove</Button>
	  </Card.Footer>
	</Card.Root>
	{/each}
	</div>
  </div>
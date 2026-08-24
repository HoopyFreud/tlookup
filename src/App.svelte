<script lang="ts">
	import './app.css';

	import * as CommandScrollbar from "$lib/components/ui/command-scrollbar/index.js";
	import * as Card from "$lib/components/ui/card/index.js";
	import * as Popover from "$lib/components/ui/popover/index.js";
	import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
	import { Separator } from "$lib/components/ui/separator/index.js";

	import { Buffer } from "buffer"

	import cardTableB64 from "$lib/cardTableb64.raw?raw";

	const cardTable = JSON.parse(Buffer.from(cardTableB64, "base64").toString())

	let buttonDOMElement: HTMLElement | null = $state(null);

	interface Card {
		name: string;
		id: string;
		keyword: string;
		text: string[];
	}

	const suitedCards = [
		{
			name: "Major Arcana",
			cards: cardTable.filter((card: Card) => card.id.charAt(0)=="M")
		},
		{
			name: "Coins",
			cards: cardTable.filter((card: Card) => card.id.charAt(0)=="C")
		},
		{
			name: "Cups",
			cards: cardTable.filter((card: Card) => card.id.charAt(0)=="U")
		},
		{
			name: "Wands",
			cards: cardTable.filter((card: Card) => card.id.charAt(0)=="W")
		},
		{
			name: "Swords",
			cards: cardTable.filter((card: Card) => card.id.charAt(0)=="S")
		}
	]

	let cardTableauArray: Array<{ name: string, id: string, keyword: string, text: Array<string>}> = $state([])

	let selectID = $state("");
	let selectCard = $derived(cardTable.find((f: Card) => f.id == selectID));

	let inputComponent:CommandScrollbar.Input;

	function resetSelectID() {
		selectID = "";
	}

	function randomSelectID() {
		selectID = cardTable[Math.floor(Math.random()*cardTable.length)].id;
	}
  
	function addToTableuClick() {
		if(selectID) {
			const newTableauCard = cardTable.find((f: Card) => f.id == selectID)
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
	<div class="h-1/2 flex flex-col">
		<!-- card selection area -->
		<CommandScrollbar.Root class="grow rounded-lg border h-auto" value={selectID} disablePointerSelection={true} vimBindings={false}>
			<CommandScrollbar.Input placeholder="Select or search for a card" cancelClickEvent={resetSelectID} shuffleClickEvent={randomSelectID} value={selectCard?.name} bind:this={inputComponent}/>
			<CommandScrollbar.List class="overflow-y-auto">
			<CommandScrollbar.Empty>No cards found</CommandScrollbar.Empty>
			{#each suitedCards as suit}
				<CommandScrollbar.Group heading={suit.name} style="font-family: Engebrechtre">
					{#each suit.cards as card}
						<CommandScrollbar.Item isSelected={selectID == card.id} onSelect={() => {selectID = card.id;}} class="text-base">
							<span>{card.name} - {card.keyword}</span>
						</CommandScrollbar.Item>
					{/each}
				</CommandScrollbar.Group>
				<CommandScrollbar.Separator />
			{/each}
			</CommandScrollbar.List>
		</CommandScrollbar.Root>

		<!-- selected card display area -->
		<div class={["overflow-y-auto",selectID?"h-1/2":"h-0"]}>
			{#if selectCard}
				<Card.Root class="overflow-y-auto max-w-full gap-0 h-full">
					<Card.Header>
						<Card.Title><h2>{selectCard.name}</h2></Card.Title>
						<Card.Description class="text-base" style="font-family: Engebrechtre">{selectCard.keyword}</Card.Description>
					</Card.Header>
					<Card.Content class="text-base">
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
		<div bind:this={buttonDOMElement}>
			<Button class="my-2 w-full" disabled={!selectID} onclick={()=>addToTableuClick()} style="font-family: Engebrechtre">Add to Tableau</Button>
		</div>
	</div>

	<!-- tableau area -->
	<div class="h-auto overflow-y-auto px-4 gap-4 flex flex-row flex-wrap justify-around">
		{#each cardTableauArray as tableauCard, tableauCardIndex}
			<Card.Root class="h-fit w-1/4 gap-4 min-h-50 min-w-50">
				<Card.Header>
					<Card.Title><h2>{tableauCard.name}</h2></Card.Title>
					<Card.Description class="text-base" style="font-family: Engebrechtre">{tableauCard.keyword}</Card.Description>
				</Card.Header>
			<Card.Content>
				<Popover.Root>
					<Popover.Trigger class={buttonVariants({ variant: "default" })} style="font-family: Engebrechtre">Description</Popover.Trigger>
					<Popover.Content class="gap-2 w-200 max-w-[75dvw] max-h-1/2" customAnchor={buttonDOMElement} side="bottom" avoidCollisions={false}>
						<Popover.Title>
							<h2>{tableauCard.name}</h2>
							<span class="text-muted-foreground" style="font-family: Engebrechtre">{tableauCard.keyword}</span>
						</Popover.Title>
							{#each tableauCard.text as textLine, lineIndex}
							<Separator/>
							<p>
								{#if lineIndex == 1}
								<b>Inverse:</b>
								{/if}
								{textLine}</p>
							{/each}
					</Popover.Content>
				</Popover.Root>
			</Card.Content>
			<Card.Footer class="place-content-center">
				<Button variant="destructive" onclick={()=>removeFromTableuClick(tableauCardIndex)} style="font-family: Engebrechtre">Remove</Button>
			</Card.Footer>
			</Card.Root>
		{/each}
	</div>
</div>
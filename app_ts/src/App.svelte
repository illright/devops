<script lang="ts">
	function getTime(timeZone: string) {
		return new Date().toLocaleTimeString(navigator.language, { timeZone })
	}
</script>

{getTime('Europe/Moscow')}

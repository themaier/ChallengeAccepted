<template>
<main>
<div class="container fullpage d-flex flex-grow-1">
    <div class="col-4 m-auto">
        <h1 class="h2 mb-3">Challenge erstellen</h1>
        <form @submit.prevent="handleSubmit">
            <div class="mb-3">
                <label class="form-label" for="challengename">Challenge Name</label>
                <input class="form-control" id="username" type="text" placeholder="z.B. Spexen" />
            </div>
            <div class="mb-3">
                <label for="selectInput">Freund auswählen</label>
                <div class="dropdown">
                    <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                        {{ selectedOption || 'Freund auswählen' }}
                    </button>
                    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                        <li><a class="dropdown-item" href="#" @click="selectOption('Sepp')">Sepp</a></li>
                        <li><a class="dropdown-item" href="#" @click="selectOption('Max')">Max</a></li>
                        <li><a class="dropdown-item" href="#" @click="selectOption('Kurt')">Kurt</a></li>
                    </ul>
                </div>
            </div>
            <div class="mb-3">
                <label for="input2">Beschreibung</label>
                <input type="text" class="form-control" id="input2" v-model="formData.input2">
            </div>

            <div class="mb-3">
                <label for="input3">Hashtag</label>
                <input type="text" class="form-control" id="input3" v-model="formData.input3">
            </div>

            <div class="mb-3">
                <label for="input4">Reward (optional)</label>
                <input type="text" class="form-control" id="input4" v-model="formData.input4">
            </div>
            <RouterLink :to="{ name: 'home' }">
                <button type="submit" class="btn btn-primary">Freund herausfordern</button>
            </RouterLink>   
        </form>
    </div>
</div>
</main>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        challengeName: '',
        friends: '',
        description: '',
        hashtags: '',
        reward: null
      },
      selectedOption: null
    };
  },
  methods: {
    handleSubmit() {
      console.log(this.formData);
    },
    selectOption(option) {
      this.selectedOption = option;
    }
  }
};
</script>



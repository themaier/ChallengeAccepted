<template>
<main>
<div class="container-md">
  <h1 class="my-4">Challenge erstellen</h1>
    <div class="col-md-5 col mt-5 m-auto">
        <form @submit.prevent="showData = true">
            <div class="mb-3">
                <label class="form-label" for="challengename">Challenge Name</label>
                <input class="form-control" id="username" type="text" v-model="formData.challengeName" placeholder="z.B. Spexen" />
            </div>
            <div class="mb-3">
              <label class="form-label" for="friendselection">Freund auswählen</label>	
                <select id="friendselection" class="form-select" v-model="formData.friends" aria-label="Default select example">
                  <option disabled value="">Wähle einen Freund aus</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="input2">Beschreibung</label>
                <input type="text" class="form-control" id="input2" v-model="formData.description">
            </div>

            <div class="mb-3">
                <label for="input3">Hashtag</label>
                <input type="text" class="form-control" id="input3" v-model="formData.hashtags">
            </div>

            <div class="mb-3">
                <label for="input4">Reward (optional)</label>
                <input type="text" class="form-control" id="input4" v-model="formData.reward">
            </div>
            <button type="submit" class="btn btn-primary">Freund herausfordern</button>

            <div v-if="showData">{{formData}}</div>
        </form>
    </div>
</div>
</main>
</template>

<script setup>
import {ref} from 'vue'

const showData = ref(false);

const formData = ref({
    challengeName: '',
    friends: '',
    description: '',
    hashtags: '',
    reward: '',
  });


</script>



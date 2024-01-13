<template>
     <div v-for="challenge in challenges" :key="challenge.id" class="modal fade modal-lg" :id="'comment' + challenge.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="modal-title h5" id="exampleModalLabel">Kommentare</h2>
                    <button class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul style="max-height:500px; overflow: auto; " class="px-0 d-flex flex-column gap-3">
                        <li v-for="comment in challenge.comments" :key="comment.id" class="d-flex">
                            <span class="fw-bold  col-2">Tobi</span>
                            <div class="col-10 d-flex flex-column gap-2 u.overflow-hidden">
                                <img v-if="comment.prove_resource_path" class="rounded " :src="comment.prove_resource_path">
                                <span v-if="comment.text">{{comment.text}}</span>
                            </div>
                        </li>
                    </ul>
                    <form>
                        <div class="mb-3">
                            <textarea class="form-control" id="exampleFormControlTextarea1" aria-label="Kommentieren" placeholder="Kommentieren..." rows="3"></textarea>
                            <input class="form-control" id="formFile" type="file" name="image" accept="image/png, image/jpg, image/jpeg" capture="user">
                        </div>
                        <button class="btn btn-primary">Kommentieren</button>   	
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, defineProps } from 'vue';

const { challenges } = defineProps(['challenges']);
</script>

<style lang="scss">
img {
    max-height:300px; 
    width:auto; 
    object-fit:contain; 
    align-self:center;

    @media screen and (max-width: 990px) {
        max-width: 200px;
    }
}
</style>
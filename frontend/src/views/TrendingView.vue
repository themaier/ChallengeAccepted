<template>
    <div class="container-md">
        <h1 class="my-4">Trends</h1>
        <input class="form-control form-control-lg mb-4" type="text" placeholder="#" aria-label="Suchen">
        <div class=" p-3 rounded">
            <h2 >#Vodka</h2>
            <div class="d-flex flex-column align-items-center gap-3">
                <div class="d-flex rounded bg-body flex-column w-100 py-2" style="max-width: 470px; max-height: 600px">
                    <div class="px-2 mb-2 d-flex justify-content-between">
                        <RouterLink :to="{ name: 'friendProfile', params: { id: 'Tobi' } }" class="col-lg-2 link-dark fw-bold link-offset-2 link-underline-opacity-0 link-underline-opacity-100-hover">Tobi</RouterLink>
                        <span>19.1.2024 17:00</span>
                    </div>
                    <img class="rounded" style="max-height:600px" src="https://images.pexels.com/photos/16452394/pexels-photo-16452394/free-photo-of-desert.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1">
                    <div class=" px-1 py-2">
                        <button  @click="like = !like" :class="{ 'icon--love--filled': like }" class="btn icon icon--love icon--size-1-5 icon--button me-2">120</button>
                        <button class="btn icon icon--comment icon--size-1-5 icon--button" data-bs-toggle="modal" data-bs-target="#comment">2</button>
                    </div>
                    <div class="px-2 fw-bold">Challenge 1</div>
                    <div class="px-2">Trinke 2 Tequila shots</div>
                    <div class="px-2"><a class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">#geil</a><a class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">#nice</a></div>
                </div>
                <div class="d-flex bg-body flex-column w-100 py-2" style="max-width: 470px">
                    <div class="px-2 mb-2 d-flex justify-content-between">
                        <RouterLink :to="{ name: 'friendProfile', params: { id: 'Tobi' } }" class="col-lg-2 link-dark fw-bold link-offset-2 link-underline-opacity-0 link-underline-opacity-100-hover">Tobi</RouterLink>
                        <span>19.1.2024 17:00</span>
                    </div>
                    <img class="rounded" style="max-height:600px" src="https://i.ibb.co/2ZxBFVp/img2.jpg">
                    <div class=" px-1 py-2">
                        <button  @click="like = !like" :class="{ 'icon--love--filled': like }" class="btn icon icon--love icon--size-1-5 icon--button me-2">120</button>
                        <button class="btn icon icon--comment icon--size-1-5 icon--button" data-bs-toggle="modal" data-bs-target="#comment">2</button>
                    </div>
                    <div class="px-2 fw-bold">Challenge 1</div>
                    <div class="px-2">Trinke 2 Tequila shots</div>
                    <div class="px-2"><a class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">#geil</a><a class="link-primary link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover">#nice</a></div>
                </div>
            </div>
        </div>
    </div>

    <div class="modal fade" id="comment" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h2 class="modal-title h5" id="exampleModalLabel">Kommentare</h2>
                    <button class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul style="max-height:500px; overflow: auto;" class="px-0">
                        <li class="d-flex justify-content-between">
                            <span class="fw-bold me-2">Tobi</span>
                            <span>Geilccccccccccyx ceeeeeeedc dsd dddddddddddddd  ffffffffffffffd     fffff</span>
                        </li>
                    </ul>
                    <form>
                        <div class="mb-3">
                            <textarea class="form-control" id="exampleFormControlTextarea1" aria-label="Kommentieren" placeholder="Kommentieren..." rows="3"></textarea>
                        </div>
                        <button class="btn btn-primary">Kommentieren</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const like = ref(false)
</script>
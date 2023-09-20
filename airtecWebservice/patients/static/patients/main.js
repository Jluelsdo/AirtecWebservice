import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'
import {OBJLoader} from 'three/examples/jsm/loaders/OBJLoader'
import Stats from 'three/examples/jsm/libs/stats.module'

const scene = new THREE.Scene()

const light = new THREE.SpotLight()
light.position.set(20, 20, 20)
scene.add(light)

const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    10000
)
camera.position.z = 300

const renderer = new THREE.WebGLRenderer()
renderer.setSize(window.innerWidth, window.innerHeight)
document.body.appendChild(renderer.domElement)

const controls = new OrbitControls(camera, renderer.domElement)
controls.enableDamping = true


const loader = new STLLoader()
const xhr = new XMLHttpRequest();
xhr.open('GET', 'load', true);
xhr.responseType = 'arraybuffer';

xhr.onload = function () {
    if (xhr.status === 200) {
        const data = xhr.response;
        const buffer = data instanceof ArrayBuffer ? data : data.buffer;
        const geometry = loader.parse(buffer);
        
        // Create a new material
        const material = new THREE.MeshNormalMaterial();

        // Create a new mesh using the loaded geometry and material
        const mesh = new THREE.Mesh(geometry, material);

        // Add the mesh to the scene
        scene.add(mesh);
    }
};
xhr.send(null);
window.addEventListener('resize', onWindowResize, false)
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    render()
}

//const stats = new Stats()
//document.body.appendChild(stats.dom)

function animate() {
    requestAnimationFrame(animate)

    controls.update()

    render()

    //stats.update()
}

function render() {
    renderer.render(scene, camera)
}

animate()
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader'
import {OBJLoader} from 'three/examples/jsm/loaders/OBJLoader'
import Stats from 'three/examples/jsm/libs/stats.module'

setTimeout( () => {
    const card = document.getElementById('stlFaceCard')
    card.style.display = 'flex';
    card.style.justifyContent = 'center';
    card.style.alignItems = 'center';
    const scene = new THREE.Scene()
    scene.add(new THREE.AxesHelper(5))

    const light = new THREE.SpotLight()
    light.position.set(20, 20, 20)
    scene.add(light)

    const camera = new THREE.PerspectiveCamera(
        75,
        card.clientWidth / card.clientHeight,
        0.1,
        1000
    )
    camera.position.y = 100
    camera.position.x = 80
    camera.position.z = 200

    const renderer = new THREE.WebGLRenderer()
    renderer.setSize(card.clientWidth, card.clientHeight)
    card.appendChild(renderer.domElement)

    const controls = new OrbitControls(camera, renderer.domElement)
    controls.enableDamping = true



    function onWindowResize() {
        camera.aspect = card.clientWidth / card.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(card.clientWidth, card.clientHeight);
    }
    onWindowResize()
    window.addEventListener('resize', onWindowResize, false)

    const loader = new STLLoader()
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/patienten/'+patientId+'/facestl', true);
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
            onWindowResize()
            animate()
        }
    }

    xhr.send(null)

    function render() {
        renderer.render(scene, camera)
    }

    function animate() {
        requestAnimationFrame(animate)
        controls.update()
        render()
    }

    animate()
}, 1000)
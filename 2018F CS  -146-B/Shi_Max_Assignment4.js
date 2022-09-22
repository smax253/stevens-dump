// Here are the paths to the images
const fileLocations = {
   woofer: './img/woofer.jpg',
   pupper: './img/pupper.jpg',
   clouds: './img/clouds.jpg',
   snek: './img/snek.jpg'
};

/**
 * This function will get the values of the following elements:
 * 		formUsername, formCaption, formImg
 * Then, this will pass those values to the addNewPost function.
 * @param {Event} event the submit event of the #postForm form
 */
function handleFormSubmit(event) {
   // This next line prevents the reload of the form
   event.preventDefault();
   // Get values of inputs
   // Pass values to addNewPost()
   if(event.type == 'submit'){
       var formelements = document.getElementById("postForm").children;
       var inputs = [];
       for(let i = 0; i<3; i++){
           inputs.push(formelements.item(i).value);
       }
       console.log(...inputs);
       addNewPost(...inputs);
   }
}

/**
 * This function create the following div and append it to the #postList element
	<div class="post">
		<span>{username}</span>
		<img src="{imgLocation}" alt="{caption}">
		<div class="postOverlay">
			{caption}
		</div>
	</div>
 * 
 * Also, add a mouseover and mouseleave events to the post div element
 * @param {String} username username of the post
 * @param {String} caption caption of the post
 * @param {String} imgLocation location of the post image
 */
function addNewPost(username, caption, imgLocation) {
    // Create the parent post div
    // Create a span for the user
    // Create image element
    // Create overlay element
    // Add all child elements (order matters)
    // Add event listeners to post
    // Add post element to post list
    
    //create post
    var post = document.createElement("div");
    post.setAttribute("class","post");
    //create username
    var user = document.createElement("span");
    user.appendChild(document.createTextNode(username));
    //create image
    var image = document.createElement("img");
    image.src = fileLocations[imgLocation];
    image.alt = caption;
    //create captions
    var imgcap = document.createElement("div");
    imgcap.appendChild(document.createTextNode(caption));
    imgcap.classList.add('postOverlay');
    imgcap.addEventListener("mouseover", event => {
        event.srcElement.style.opacity = 1
    })
    imgcap.addEventListener("mouseleave", event => {
        event.srcElement.style.opacity = 0
    });
    //append to post and postlist
    post.append(user, image, imgcap);
    document.getElementById("postList").appendChild(post);
}

window.onload = () => {
   // Once our window is loaded, we add the event listener for our post form
   postForm.addEventListener('submit', handleFormSubmit);
};
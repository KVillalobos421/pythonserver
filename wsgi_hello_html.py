from wsgiref.simple_server import make_server

# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object (see PEP 333).
def hello_world_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/html; charset=utf-8')]  # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    return [b"""<!DOCTYPE html>
<html>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body, h1,h2,h3,h4,h5,h6 {font-family: "Montserrat", sans-serif}
.w3-row-padding img {margin-bottom: 12px}
.bgimg {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    background-image: url('https://www.w3schools.com/w3images/profile_girl.jpg');
    min-height: 100%;
 }
</style>

<body>

<!-- Sidebar with image -->
<nav class="w3-sidebar w3-hide-medium w3-hide-small" style="width:40%">
  <div class="bgimg"></div>
</nav>

<!-- Hidden Sidebar (reveals when clicked on menu icon)-->
<nav class="w3-sidebar w3-black w3-animate-right w3-xxlarge" style="display:none;padding-top:150px;right:0;z-index:2" id="mySidebar">
  <a href="javascript:void(0)" onclick="closeNav()" class="w3-button w3-black w3-xxxlarge w3-display-topright" style="padding:0 12px;">
    <i class="fa fa-remove"></i>
  </a>
  <div class="w3-bar-block w3-center">
    <a href="#" class="w3-bar-item w3-button w3-text-grey w3-hover-black" onclick="closeNav()">Home</a>
    <a href="#portfolio" class="w3-bar-item w3-button w3-text-grey w3-hover-black" onclick="closeNav()">Portfolio</a>
    <a href="#about" class="w3-bar-item w3-button w3-text-grey w3-hover-black" onclick="closeNav()">About</a>
    <a href="#contact" class="w3-bar-item w3-button w3-text-grey w3-hover-black" onclick="closeNav()">Contact</a>
  </div>
</nav>

<!-- Page Content -->
<div class="w3-main w3-padding-large" style="margin-left:40%">

  <!-- Menu icon to open sidebar -->
  <span class="w3-button w3-top w3-white w3-xxlarge w3-text-grey w3-hover-text-black" style="width:auto;right:0;" onclick="openNav()"><i class="fa fa-bars"></i></span>

  <!-- Header -->
  <header class="w3-container w3-center" style="padding:128px 16px" id="home">
    <h1 class="w3-jumbo"><b>Diane Lahm</b></h1>
    <p>Software Developer and Steamer.</p>
    <img src="https://www.w3schools.com/w3images/profile_girl.jpg" class="w3-image w3-hide-large w3-hide-small w3-round" style="display:block;width:60%;margin:auto;">
    <img src="https://www.w3schools.com/w3images/profile_girl.jpg" class="w3-image w3-hide-large w3-hide-medium w3-round" width="1000" height="1333">
    <button class="w3-button w3-light-grey w3-padding-large w3-margin-top">
      <i class="fa fa-download"></i> Load Resume
    </button>
  </header>

  <!-- Portfolio Section -->
  <div class="w3-padding-32 w3-content" id="portfolio">
    <h2 class="w3-text-grey">My Portfolio</h2>
    <hr class="w3-opacity">

    <!-- Grid for photos -->
    <div class="w3-row-padding" style="margin:0 -16px">
      <div class="w3-half">
        <img src="https://www.w3schools.com/w3images/wedding.jpg" style="width:100%">
        <img src="https://www.w3schools.com/w3images/rocks.jpg" style="width:100%">
        <img src="https://www.w3schools.com/w3images/sailboat.jpg" style="width:100%">
      </div>

      <div class="w3-half">
        <img src="https://www.w3schools.com/w3images/underwater.jpg" style="width:100%">
        <img src="https://www.w3schools.com/w3images/chef.jpg" style="width:100%">
        <img src="https://www.w3schools.com/w3images/wedding.jpg" style="width:100%">
        <img src="https://www.w3schools.com/w3images/p6.jpg" style="width:100%">
      </div>
    <!-- End photo grid -->
    </div>
  <!-- End Portfolio Section -->
  </div>

  <!-- About Section -->
  <div class="w3-content w3-justify w3-text-grey w3-padding-32" id="about">
    <h2>About</h2>
    <hr class="w3-opacity">
    <p> I am a full time Software Developer in Activision, on my freetime I enjoy streaming, I meet new people,network and enjoy learning many new things for programing or video games. 
    </p>
    <h3 class="w3-padding-16">My Skills</h3>
    <p class="w3-wide">Software Developing</p>
    <div class="w3-light-grey">
      <div class="w3-container w3-center w3-padding-small w3-dark-grey" style="width:95%">95%</div>
    </div>
    <p class="w3-wide">Streaming</p>
    <div class="w3-light-grey">
      <div class="w3-container w3-center w3-padding-small w3-dark-grey" style="width:82%">85%</div>
    </div>
    <p class="w3-wide">Sleeping</p>
    <div class="w3-light-grey">
      <div class="w3-container w3-center w3-padding-small w3-dark-grey" style="width:65%">80%</div>
    </div><br>

    <div class="w3-row w3-center w3-dark-grey w3-padding-16 w3-section">
      <div class="w3-quarter w3-section">
        <span class="w3-xlarge">10+</span><br>
        Partners
      </div>
      <div class="w3-quarter w3-section">
        <span class="w3-xlarge">125+</span><br>
        Projects Done
      </div>
      <div class="w3-quarter w3-section">
        <span class="w3-xlarge">25,000+</span><br>
        Happy Clients
      </div>
      <div class="w3-quarter w3-section">
        <span class="w3-xlarge">200+</span><br>
        Meetings
      </div>
    </div>

    <button class="w3-button w3-light-grey w3-padding-large w3-section">
      <i class="fa fa-download"></i> Load Resume
    </button>

    <!-- Testimonials -->
    <h3 class="w3-padding-24">My Reputation</h3>
    <img src="https://www.w3schools.com/w3images/avatar_smoke.jpg" alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:80px">
    <p><span class="w3-large w3-text-black w3-margin-right">Ben Dover.</span> Software Engineer.</p>
    <p>Diane Lahm is just awesome. I am so happy to have met her and learn so much from her! </p><br>
   
    <img src="https://www.w3schools.com/w3images/bandmember.jpg" alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:80px">
    <p><span class="w3-large w3-text-black w3-margin-right">Chris Bopkins.</span> CEO at Activision.</p>
    <p>Diane Lahm has saved us from many software issues and has made our life easier in the company.</p><br>
    
    <img src="https://www.w3schools.com/w3images/avatar_g2.jpg" alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:80px">
    <p><span class="w3-large w3-text-black w3-margin-right">Lauren Flaun.</span> Software Develop Manager.</p>
    <p>No one is better than Diane Lahm, she was a great choice.</p><br>
    
    <!-- Grid for pricing tables -->
    <h3 class="w3-padding-16">My Price</h3>
    <div class="w3-row-padding" style="margin:0 -16px">
      <div class="w3-half w3-margin-bottom">
        <ul class="w3-ul w3-center w3-card w3-hover-shadow">
          <li class="w3-dark-grey w3-xlarge w3-padding-32">Basic</li>
          <li class="w3-padding-16">Software Programs</li>
          <li class="w3-padding-16">Web Developing</li>
          <li class="w3-padding-16">5GB Storage</li>
          <li class="w3-padding-16">Mail Support</li>
          <li class="w3-padding-16">
            <h2>$ 10</h2>
            <span class="w3-opacity">per month</span>
          </li>
          <li class="w3-light-grey w3-padding-24">
            <button class="w3-button w3-white w3-padding-large w3-hover-black">Sign Up</button>
          </li>
        </ul>
      </div>

      <div class="w3-half">
        <ul class="w3-ul w3-center w3-card w3-hover-shadow">
          <li class="w3-black w3-xlarge w3-padding-32">Pro</li>
          <li class="w3-padding-16">Software Programs</li>
          <li class="w3-padding-16">Web Developing</li>
          <li class="w3-padding-16">50GB Storage</li>
          <li class="w3-padding-16">Endless Support</li>
          <li class="w3-padding-16">
            <h2>$ 25</h2>
            <span class="w3-opacity">per month</span>
          </li>
          <li class="w3-light-grey w3-padding-24">
            <button class="w3-button w3-white w3-padding-large w3-hover-black">Sign Up</button>
          </li>
        </ul>
      </div>
    <!-- End Grid/Pricing tables -->
    </div>
    
  <!-- End About Section -->
  </div>

  <!-- Contact Section -->
  <div class="w3-padding-32 w3-content w3-text-grey" id="contact" style="margin-bottom:64px">
    <h2>Contact Me</h2>
    <hr class="w3-opacity">

    <div class="w3-section">
      <p><i class="fa fa-map-marker fa-fw w3-xxlarge w3-margin-right"></i> Chicago, IL.</p>
      <p><i class="fa fa-phone fa-fw w3-xxlarge w3-margin-right"></i> Phone: +222 1515151</p>
      <p><i class="fa fa-envelope fa-fw w3-xxlarge w3-margin-right"> </i> Email: DLahmDeveloper@mail.com</p>
    </div>
    
     <!-- Google Map -->
    <div id="googleMap" class="w3-greyscale-max" style="width:100%;height:300px;margin:36px 0;"></div>
   
    <p>Lets get in touch. Send me a message:</p>
    <form action="https://www.maps.googleapis.com/action_page.php" target="_blank">
      <p><input class="w3-input w3-padding-16 w3-border" type="text" placeholder="Name" required name="Name"></p>
      <p><input class="w3-input w3-padding-16 w3-border" type="text" placeholder="Email" required name="Email"></p>
      <p><input class="w3-input w3-padding-16 w3-border" type="text" placeholder="Subject" required name="Subject"></p>
      <p><input class="w3-input w3-padding-16 w3-border" type="text" placeholder="Message" required name="Message"></p>
      <p>
        <button class="w3-button w3-light-grey w3-padding-large" type="submit">
          <i class="fa fa-paper-plane"></i> SEND MESSAGE
        </button>
      </p>
    </form>
  <!-- End Contact Section -->
  </div>  
  
  <!-- Footer -->
  <footer class="w3-container w3-padding-64 w3-light-grey w3-center w3-opacity w3-xlarge" style="margin:-24px">
    <i class="fa fa-facebook-official w3-hover-opacity"></i>
    <i class="fa fa-instagram w3-hover-opacity"></i>
    <i class="fa fa-snapchat w3-hover-opacity"></i>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
    <p class="w3-medium">Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank" class="w3-hover-text-green">w3.css</a></p>
  <!-- End footer -->
  </footer>
  
<!-- END PAGE CONTENT -->
</div>

<!-- Add Google Maps -->
<script>
function myMap()
{
  myCenter=new google.maps.LatLng(41.878114, -87.629798);
  var mapOptions= {
    center:myCenter,
    zoom:12, scrollwheel: false, draggable: false,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  var map=new google.maps.Map(document.getElementById("googleMap"),mapOptions);

  var marker = new google.maps.Marker({
    position: myCenter,
  });
  marker.setMap(map);
}

// Open and close sidebar
function openNav() {
    document.getElementById("mySidebar").style.width = "60%";
    document.getElementById("mySidebar").style.display = "block";
 }

function closeNav() {
    document.getElementById("mySidebar").style.display = "none";
 }
</script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBu-916DdpKAjTmJNIgngS6HL_kDIKU0aU&callback=myMap"></script>
<!--
To use this code on your website, get a free API key from Google.
Read more at: https://www.w3schools.com/graphics/google_maps_basic.asp
-->

</body>
</html>
"""]

with make_server('', 8000, hello_world_app) as httpd:
    print("Loading Up Port 8000... Head to the Objective...")

    # Serve until process is killed
    httpd.serve_forever()
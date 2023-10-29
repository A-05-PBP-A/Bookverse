const stars = document.querySelectorAll('.star');
    let selectedRating = 0;

    stars.forEach(star => {
        star.addEventListener('mouseover', () => {
            const rating = star.getAttribute('data-rating');
            stars.forEach(s => {
                s.classList.remove('active');
                if (s.getAttribute('data-rating') <= rating) {
                    s.classList.add('active');
                }
            });
        });

        star.addEventListener('mouseout', () => {
            stars.forEach(s => s.classList.remove('active'));
            if (selectedRating > 0) {
                stars.forEach(s => {
                    if (s.getAttribute('data-rating') <= selectedRating) {
                        s.classList.add('active');
                    }
                });
            }
        });

        star.addEventListener('click', () => {
            const rating = star.getAttribute('data-rating');
            selectedRating = rating;
            stars.forEach(s => {
                s.classList.remove('active');
                if (s.getAttribute('data-rating') <= rating) {
                    s.classList.add('active');
                }
            });
        });
    });

    var scrollContainer = document.getElementById('bookScroll');

    function scrollRight() {
        scrollContainer.scrollBy({ left: 960, behavior: 'smooth' });
    }

    function scrollRight2() {
        scrollContainer.scrollBy({ left: -960, behavior: 'smooth' });
    }

    async function getAverageRating() {
        const reviews = await getReview();
        let totalRating = 0;
        if (reviews.length > 0) {
            reviews.forEach((item) => {
                totalRating += item.fields.rating;
            });
            return totalRating / reviews.length;
        } else {
            return 0;
        }
    }

    async function displayAverageRating() {
        const averageRating = await getAverageRating();
        const reviews = await getReview();
        const starsElement =  document.getElementById("average-rating");
        let stars = '';
        for(let i=1; i<=5; i++){
            if(i <= Math.round(averageRating)){
                stars += '<span style="color: orange;">★</span>';
            } else {
                stars += '<span style="color: gray;">★</span>';
            }
        }
        starsElement.innerHTML = `${stars} ${averageRating.toFixed(2)} <span style="color: #888888; font-size: 15px; position: relative; top: -3px;">${reviews.length} Ratings</span>`;
    }

    async function getReview() {
        const bookId = "{{ book.id }}"; 
        return fetch(`/get_review_json/${bookId}`).then((res) => res.json())  
    }

    async function refreshReviews() {
        document.getElementById("review_table").innerHTML = ""
        const review = await getReview()
        let htmlString = ''
        if (review.length > 0) {
            review.forEach((item) => {
                let stars = '';
                for(let i=0; i<5; i++){
                    if(i<item.fields.rating){
                        stars += '<span style="color: orange;">★</span>';
                    } else {
                        stars += '<span style="color: gray;">★</span>';
                    }
                }
                htmlString += `
                <div class="card mb-3" style="width: 58em; border: none;">
                    <div class="row no-gutters align-items-center">
                        <div class="col-md-1">
                            <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png" class="card-img" alt="profile" style="max-width: 100px;">
                        </div>
                        <div class="col-md-11">
                            <div class="card-body">
                                <h5 class="card-title">Rating: ${stars}</h5>
                                <p class="card-text">${item.fields.review}</p>
                            </div>
                            <hr>
                        </div>
                    </div>
                </div>` 
            })
        } else {
            htmlString = `
            <div class="alert alert-info" role="alert">
                Maaf, belum ada review yang tersedia untuk buku ini. Jadilah yang pertama untuk memberikan review!
            </div>`;
        }
        
        document.getElementById("review_table").innerHTML = htmlString
        displayAverageRating();
    }
    refreshReviews()
    
    function addReview() {
        const rating = selectedRating;
        const bookId = "{{ book.id }}";

        // Cek apakah rating dan review kosong
        if (!rating) {
            document.getElementById("ratingWarning").textContent = "Rating harus diisi!";
            return false;
        } else {
            document.getElementById("ratingWarning").textContent = "";
        }

        const formData = new FormData(document.querySelector('#form'));
        formData.append('rating', rating);
        formData.append('book_id', bookId);
        
        fetch("{% url 'bookProfile:add_review_ajax' %}", {
            method: "POST",
            body: formData
        }).then(refreshReviews);

        document.getElementById("form").reset();
        return false;
    }
    document.getElementById("button_add").onclick = addReview
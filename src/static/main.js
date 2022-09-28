
let visible = 3



window.onload = function(){
    const articlesBox = document.getElementById('articles-box')
    const loadBtn = document.getElementById('load-btn')
    const spinnerBox = document.getElementById('spinner-box')
    
    const handleGetData = () => {
        $.ajax({
            type: 'GET',
            url: `/articles-json/${visible}`,
            success: function(response){
                //console.log(response.max)
                maximum_size = response.max
                const data = response.data
                spinnerBox.classList.remove('not-visible')
                setTimeout(()=>{
                    spinnerBox.classList.add('not-visible')
                    data.map(article=>{
                        console.log(article.id)
                        articlesBox.innerHTML += `<div class="card p-3 mt-3 mb-3">
                                                ${article.title}
                                                <br>
                                                ${article.source}
                                                <br>
                                                ${article.date}
                                            </div>`
                    })
                },500)
                
                if(maximum_size){
                    console.log('Done')
                }
            },
            error: function(error){
                console.log(error)
            }
        })
    
    }

    handleGetData()

    loadBtn.addEventListener('click', ()=>{
        visible += 3
        handleGetData()
    })
}



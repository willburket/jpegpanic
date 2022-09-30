
let visible = 9



window.onload = function(){
    const articlesBox = document.getElementById('articles-box')
    const loadBtn = document.getElementById('load-btn')
    const spinnerBox = document.getElementById('spinner-box')
    const contentBox = document.getElementById('content-box')
    
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
                        articlesBox.innerHTML += `<div class="card">
                        <button id="content-btn" type="button" class="btn btn-secondary btn-sm btn-block text-nowrap text-truncate w-100" style="border-radius: 8px; height: 75px;"> 
                                    ${article.title}
                                    <br>
                                    ${article.author}
                                    <br>
                                    ${article.date}
                        </button>
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
    const contentBtn = document.getElementById('content-btn')

    // contentBtn.addEventListener('click', ()=>{

    // })

    handleGetData()

    loadBtn.addEventListener('click', ()=>{
        visible += 10
        handleGetData()
    })

    
}   




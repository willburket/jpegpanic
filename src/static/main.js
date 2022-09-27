
let visible = 3

const articlesBox = document.getElementById('articles-box')

window.onload = function(){
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
                    data.map(post=>{
                        console.log(post.id)
                    })
                ,500})
                
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



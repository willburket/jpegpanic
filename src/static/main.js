// console.log('sup boh')

$.ajax({
    type: 'GET',
    url: '/articles-json/',
    success: function(response){
        // console.log(response.data)
        const data = response.data
        data.map(post=>{
            console.log(post.id)
        })
    },
    error: function(error){
        console.log(error)
    }
})

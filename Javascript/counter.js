 let counter=0;
            function updatedispaly(){
                document.querySelector('h1').innerHTML="count:"+counter
            }
            function increment(value){
                counter+=value;
                updatedispaly()
                if(counter % 10 === 0){
                    alert(`count is now${counter}`)
                }
            }
            function reset(){
                counter=0;
                updatedispaly()
            }
            document.addEventListener("DOMContentLoaded", function (){
                document.querySelector('#add1').addEventListener("click",function(){
                    increment(1)
                })
                document.querySelector('#add5').addEventListener("click",function(){
                    increment(5)
                })
                document.querySelector('#reset').addEventListener("click",function(){
                    reset()
                })
            })

$(document).ready(function(){
	var urlsList = []	
	$('#spi_sak').click(function(){
		console.log('Hello');
		var id = $(this).data('id');
		$('.inside_box2_slajder').remove()
        if (!urlsList.includes(id)){ 
        	urlsList.push(id);
        	var list_html = ''; 
        	Url = "/" + id
        	$.ajax({
				'async': false,     //ajax request doesn't work without this line, but this apparently is not the best solution.
				url: Url,
				type: 'GET',
				// contentType: 'application/json',
				dataType: 'json',
				success: function(result) { 

					// console.log(result);
					var i = 0;
					var count = 0;
					list_html = "<div class=\"inside_box2_slajder\">"
					while(i < result.new_list.length){
			
	                    for(i; i < i + 5; i++){
	                    	console.log(count);
	                    	console.log("This is i :", count);

	                    	try{
		                    	if(count == 0){                     //beggining of the slide
								    list_html += `<div class=\"inside_box2\" style=\"margin-bottom: 30px;\">
								                     <p class=\"title\">Spisak Žrtava</p>" 
			                                         <div class="clanak">
							        				      <div class="levi">
							        				          <img src="` + result.new_list[i]['image'] +  `">
							        				      </div>
										        		  <div class="desni">
										        			<div class="gornji">Otac Marijane Kalderon šalje pismo supruzi Fani i deci iz Topovskih šupa, oktobar 1941.</div>
										        			<div class="srednji">Jevrejski istorijski muzej, k. 24-2a (kasa)</div>
										        			<div class="donji">
										        				<div class="d_levi">
										        				    <p>DOWNLOAD</p>
										        			    </div>
										        				<a href="#">
										        					<div class="d_desni"><img src="{% static 'topovske/images/bela_strelica.png' %}"></div>
										        				</a>
										        			</div>
										        		  </div>
										        	    <br style="clear: both;">
										             </div>`;	//clanak	
								    console.log("***********************************")
								    console.log("Count: ", count);
								    console.log("LIST_HTML: ");
								    console.log(list_html);	
								    count += 1;	
								} else if(count == 4 || i == result.new_list.length - 1){                 //end of the slide
		                            list_html += `<div class="clanak">
							        				<div class="levi">
							        				    <img src="` + result.new_list[i]['image'] +  `">
							        				</div>
										        		<div class="desni">
										        			<div class="gornji">Otac Marijane Kalderon šalje pismo supruzi Fani i deci iz Topovskih šupa, oktobar 1941.</div>
										        			<div class="srednji">Jevrejski istorijski muzej, k. 24-2a (kasa)</div>
										        			<div class="donji">
										        				<div class="d_levi">
										        				    <p>DOWNLOAD</p>
										        			    </div>
										        				<a href="#">
										        					<div class="d_desni"><img src="{% static 'topovske/images/bela_strelica.png' %}"></div>
										        				</a>
										        			</div>
										        		</div>
										            <br style="clear: both;">
										          </div>`; //clanak	
								    list_html += "</div>"; //inside_box2
								    count = 0;
								    
								    console.log("***********************************")
								    console.log("Count: ", count);
								    console.log("LIST_HTML: ");
								    console.log(list_html);		
								} else {                               //body of the slide
									list_html += `<div class="clanak">
							        				<div class="levi">
							        				    <img src="` + result.new_list[i]['image'] +  `">
							        				</div>
										        		<div class="desni">
										        			<div class="gornji">Otac Marijane Kalderon šalje pismo supruzi Fani i deci iz Topovskih šupa, oktobar 1941.</div>
										        			<div class="srednji">Jevrejski istorijski muzej, k. 24-2a (kasa)</div>
										        			<div class="donji">
										        				<div class="d_levi">
										        				    <p>DOWNLOAD</p>
										        			    </div>
										        				<a href="#">
										        					<div class="d_desni"><img src="{% static 'topovske/images/bela_strelica.png' %}"></div>
										        				</a>
										        			</div>
										        		</div>
										        	 <br style="clear: both;">
										          </div>`;	//clanak
	
								    console.log("***********************************")
								    console.log("Count: ", count);
								    console.log("LIST_HTML: ");
								    console.log(list_html);	
								    count += 1;						
								}
								
							} 
							catch(err){
								break
							} 
						     
	                    } //for loop end
                       

	                    i += 5;
	                    
	                    console.log("This is count:::::::  ", count);
	                  

                        list_html += "</div>";
                    }
                    console.log(list_html)
                    
                    $('.arhiva_container').append(list_html);
                    $('.inside_box2_slajder').slick('reinit');
                    $(this).css('color', '#324E6B');
                    $(this).siblings().css('visibility', 'visible')
                    if(!urlsList.length == 0){
                    	$(`div[data-id="${urlsList[0]}"`).css('color', '#9BA7B1');
                    	$(`div[data-id="${urlsList[0]}"`).siblings('visibility', 'hidden');
                    }
                    urlsList.push(id);
                   
					
				}
               
            });
                   
        }


    })

});
// function sliderInit(){
// 					    $('.inside_box2_slajder').slick({
// 							slidesToShow: 1,
// 							slidesToScroll: 1,
// 							arrows: true,
// 							dots: true,
// 							infinite: false,
// 							// prevArrow: $('.prev'),
// 							// nextArrow: $('.next')
// 					    });
// 					};
					// sliderInit();








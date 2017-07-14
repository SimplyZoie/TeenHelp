TweenMax.set('li', {z:0.1, opacity:0.999, scale:1});

var dur = 3
TweenMax.staggerTo('li:nth-of-type(odd)', dur, {fontSize:'+=4vw', repeat:-1, yoyo:true}, .3)
TweenMax.to('li:nth-of-type(1)', dur, {fontSize:'+=3vw', repeat:-1, yoyo:true})
TweenMax.to('li:nth-of-type(2)', dur, {fontSize:'-=2vw', repeat:-1, yoyo:true})
TweenMax.to('li:nth-of-type(3)', dur, {fontSize:'+=4vw', repeat:-1, yoyo:true})

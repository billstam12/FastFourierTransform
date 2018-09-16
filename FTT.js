const math = require("mathjs");

function rand(){
  return math.floor((math.random() * 20) + 1);
}

var numSamples = 16; // Must be power of 2
var freqs = [2, 5, 11, 17, 29]; /* Known frequencies for testing */
var x = []
var X =[]
for(var i = 0; i < numSamples; i++){
  x.push(math.complex(0,0));

  for(var j = 0; j< freqs.length; j++){
    const sine = math.sin(2*math.pi*freqs[j]*i/numSamples);
    x[i] = math.add(x[i], sine);
  }
X[i] = x[i];
}
console.log(X);
X = fastFourierTransform(X,numSamples);
console.log(X);

function seperate(X){
  var odds = [];
  var evens = [];
  for (var i = 0; i< X.length; i++){
    if(i % 2 == 0){
      evens.push(X[i]);
    }
    else{
      odds.push(X[i]);
    }
  }
  return [evens, odds];
}

/* Compute F.F.T */

function fastFourierTransform(X,numSamples){
	if(numSamples >= 2){
		sortX = seperate(X); // Seperate odds from evens
		evens = sortX[0];
		odds = sortX[1];
			/* Recurse for the bottom half, and the upper half
			and then apply the fft equations to each according to its type */

		fastFourierTransform(evens,numSamples/2);
		fastFourierTransform(odds,numSamples/2);


		for( var k = 0; k < numSamples/2; k++){
			e = evens[k];
			o  = evens[k];

			w = math.exp(math.complex(0, -2* math.pi*k/numSamples));
			X[k] = math.add(math.multiply(w,o),e);
			X[k+numSamples/2] = math.subtract(math.multiply(w,o),e)
		}
	
	}
	else{

	}
	return X;
}

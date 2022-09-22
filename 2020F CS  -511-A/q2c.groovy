
/*
Quiz 2C - 25 Sep 2020

You may not add print statements nor additional semaphores.
Add ONLY acquire and release operations to the following code so that the output is:

aabcaabcaabc....

*/

import java.util.concurrent.Semaphore;
Semaphore a = new Semaphore(0);
Semaphore b = new Semaphore(0);
Semaphore c = new Semaphore(2);



Thread.start { // P

    while (true) {
    c.acquire();
	print("a");
    a.release();
    }
}

Thread.start { // Q 

    while (true) {
    a.acquire(2);
	print("b");
    b.release();
    }
}


Thread.start { // R

    while (true) {
    b.acquire();
	print("c");
    c.release(2);
    }
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "operands could not be broadcast together with shapes (4,) (100,) (4,) ",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-13-5f28594dbd6a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     38\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     39\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 40\u001b[0;31m \u001b[0mmaximo\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msigma\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmaximo_sigma\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprior\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mposterior\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmu\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     41\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-13-5f28594dbd6a>\u001b[0m in \u001b[0;36mposterior\u001b[0;34m(H, secuencia)\u001b[0m\n\u001b[1;32m     21\u001b[0m     \u001b[0mPosterior\u001b[0m \u001b[0mcalculado\u001b[0m \u001b[0mcon\u001b[0m \u001b[0mla\u001b[0m \u001b[0mnormalizacion\u001b[0m \u001b[0madecuada\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m     \"\"\"\n\u001b[0;32m---> 23\u001b[0;31m     \u001b[0mpost\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlike\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msigma\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mmu\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprior\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmu\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     24\u001b[0m     \u001b[0mevidencia\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mamax\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpost\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     25\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexp\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpost\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mevidencia\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mtrapz\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexp\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpost\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mevidencia\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mmu\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-13-5f28594dbd6a>\u001b[0m in \u001b[0;36mlike\u001b[0;34m(secuencia, sigma, mu)\u001b[0m\n\u001b[1;32m     14\u001b[0m     \u001b[0mL\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mzeros\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 16\u001b[0;31m         \u001b[0mL\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1.\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msqrt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2.0\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpi\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0msigma\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexp\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m0.5\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msecuencia\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mmu\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m/\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msigma\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     17\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mL\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     18\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: operands could not be broadcast together with shapes (4,) (100,) (4,) "
     ]
    }
   ],
   "source": [
    "\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "x =[4.6, 6.0, 2.0, 5.8] \n",
    "x=np.array(x)\n",
    "sigma =[2.0, 1.5, 5.0, 1.0]\n",
    "mu=np.array(mu)\n",
    "mu=np.linspace(10,-10,100)\n",
    "\n",
    "def prior(a):\n",
    "    p=np.ones(len(a))\n",
    "    return p\n",
    "\n",
    "def like(secuencia, sigma,mu):\n",
    "    L=np.zeros(len(x))\n",
    "    for i in range(len(x)):\n",
    "        L += np.log(1./np.sqrt(2.0*np.pi*sigma[i]**2))*np.exp(-0.5*(secuencia[i]-mu)**2/(sigma[i]**2))\n",
    "    return L\n",
    "\n",
    "def posterior(H, secuencia):\n",
    "    \"\"\"\n",
    "    Posterior calculado con la normalizacion adecuada\n",
    "    \"\"\"\n",
    "    post = like(x, sigma,mu) + np.log(prior(mu))\n",
    "    evidencia = np.amax(post)\n",
    "    return np.exp(post-evidencia)/trapz(np.exp(post-evidencia),mu)\n",
    "    \n",
    "\n",
    "def maximo_sigma(x, y):\n",
    "    deltax = x[1] - x[0]\n",
    "\n",
    "    ii = np.argmax(y)\n",
    "\n",
    "    # segunda derivada\n",
    "    d = (y[ii+1] - 2*y[ii] + y[ii-1]) / (deltax**2)\n",
    "\n",
    "    return x[ii], 1.0/np.sqrt(-d)\n",
    "    \n",
    "\n",
    "\n",
    "maximo, sigma = maximo_sigma(prior(x), posterior(mu,x))\n",
    "\n",
    "\n",
    "\n",
    "plt.figure()\n",
    "plt.plot(H, post, label='datos={}'.format(secuencia))\n",
    "plt.plot(H, gauss, ':', label='Aproximacion Gaussiana')\n",
    "plt.title('H= {:.2f} $\\pm$ {:.2f}'.format(max, sigma))\n",
    "plt.xlabel('H')\n",
    "plt.ylabel('prob(H|datos)')\n",
    "plt.legend()\n",
    "plt.savefig('coins')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

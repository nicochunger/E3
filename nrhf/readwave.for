	program readwave			!!!     17 Feb 2016

c..... read fort.1 (nrhf output) and print wavefunctions


      implicit real*8(a-h,o-z)
      parameter(NOR=30,NGP=500,NSCAL=10)
      character*4 idn,lab
      common/radial/r(NGP),rp(NGP),rpor(NGP),h
      common/labdat/idn,lab(NOR)
      common/intdat/jx,jz,jc,ns(NOR),ls(NOR),js(NOR),ms(NOR),ks(NOR)
      common/fixdat/wi(NOR),wf(NOR)
      common/wavefn/p(NGP,NOR),q(NGP,NOR)


c.... read file
      open(unit=1,file='fort.1',form='unformatted',status='old')
      rewind 1
      read(1) idn,jz,jx,jc
      read(1) r,rp,rpor,h
      do 100 ia = 1,jx
          read(1) ns(ia),ls(ia),ms(ia),lab(ia),wf(ia)
          read(1) (p(i,ia),i=1,NGP)
100   continue


	do 500 ia=1,jx
	  open(unit=10,file='wave.'//lab(ia)(2:3),status='unknown')
	  do 400 i=1,NGP
		write(10,*) r(i),' ',p(i,ia)
400	  continue
	  close(10)
500	continue

	stop
	end

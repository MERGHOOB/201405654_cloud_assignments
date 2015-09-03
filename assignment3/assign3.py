from mininet.topo import Topo

class MyTopo( Topo ):

	def __init__(self):

		Topo.__init__(self)

		nos=input('Enter the no of Switch ')
		noh=input('Enter no of host ')


		s_stm='sw'
		swt=[]
		for i in range(nos):
			tmp=s_stm+str(i+1)
			swt.append(tmp)

		s_host='host'
		host_list=[]
		for i in range(1,(noh*nos)+1):
			tmp=s_host+str(i)
			host_list.append(tmp)
	
		hl=[]
		j=1
		k=1
		counter=1
		ip_even='10.0.0.'
		ip_odd='12.1.0.'

		for i in host_list:	
			if counter%2==0 :
				qq="\'"+ip_even+str(j)+"\'"
				print qq
				a=self.addHost(i,ip=qq)
				j=j+1
			else:
				qq="\'"+ip_odd+str(k)+"\'"
				print qq
				a=self.addHost(i,ip=qq)
				k=k+1
			hl.append(a)
			counter=counter+1

		sl=[]
		for i in swt:
			a=self.addSwitch(i)
			sl.append(a)

		j=0
		for i in range(0,len(sl)):
			if i+1 != len(sl):
				self.addLink(sl[i],sl[i+1])
			k=0
			while k<noh : 
				if k%2==0:
					self.addLink(sl[i],hl[j], bw=1 )
				else:
					self.addLink(sl[i],hl[j], bw=2 )
				k=k+1
				j=j+1

topos= {'mytopo' : (lambda: MyTopo() )}



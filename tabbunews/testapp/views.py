from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movienews_view(request):
    news1 = 'In Hollywood Avenger End Game is Biggest Blockbuster Hit'
    news2 = 'Salman khan is Going To Be Married Soon'
    news3 = 'Sharukh Khan Is The Biggest Richest Man Among All Heroes'
    news4 = 'My Wife Is going 2 Give Birth InshaAllah in Novem ber'
    my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/mnews.html',my_dict )

def sportsnews_view(request):
    news5 = 'In Cricket IPL is the Most watched game in India'
    news6 = 'Andre Russel is the Man on the math in IPL'
    news7 = 'In This World Cup India has performed Very Much Worst'
    news8 = 'My Wife Is My Life, i cant imagine My life without Her'
    my_dict1 = {'news5':news5,'news6':news6,'news7':news7,'news8':news8}
    return render(request,'testapp/snews.html',my_dict1 )

def mobilenews_view(request):
    news1 = 'In Mobie Mi is The Best Selling Mobile in India'
    news2 = 'Mi4i Is the Best Mobile in the world'
    news3 = 'In This World Android is the biggest platform for Tecgnology'
    news4 = 'My Wife Is My Life, i cant imagine My life without Her'
    my_dict2 = {'news1':news1,'news2':news2,'news3':news3,'news4':news4}
    return render(request,'testapp/mobilenews.html',my_dict2 )
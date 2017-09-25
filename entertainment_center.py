import media
import fresh_tomatoes

detachment = media.Movie('Detachment',
                         'http://i-7.vcimg.com/crop/b325472483e527b16a01a1ce106dc18a1220498(600x)/thumb.jpg',
                         'https://youtu.be/I-gS8OBt-yk'
                         )

pianist = media.Movie('Pianist',
                      'http://image.xcar.com.cn/attachments/a/day_121208/2012120817_faf5b0a123d5a9c2e7b30CtCZJTt25RJ.jpg',
                      'https://youtu.be/BFwGqLa_oAo'
                      )

her = media.Movie('Her',
                  'http://imgsrc.baidu.com/forum/pic/item/38d12f2eb9389b506e63848e8035e5dde6116e49.jpg',
                  'https://youtu.be/ne6p6MfLBxc'
                  )

romeo_must_die = media.Movie('Romeo Must Die',
                             'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1495887632341&di=9ca14c4245a08f2a679ba0de56ce8a70&imgtype=0&src=http%3A%2F%2Fimg31.mtime.cn%2Fpi%2F2014%2F03%2F06%2F081651.89999120_220X220.jpg', 
                             'https://youtu.be/NJkuK94a5vs'
                             )

transcendence = media.Movie('Transcendence',
                            'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1496482707&di=899bd1fb16eb62222b8651ae2e0f247d&imgtype=jpg&er=1&src=http%3A%2F%2Fimgwx3.2345.com%2Fdianyingimg%2Fimg%2F9%2F34%2Fsup103774_223x310.jpg%3Fv2015081107',
                            'https://youtu.be/QheoYw1BKJ4'
                            )

buried = media.Movie('Buried',
                     'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1495888517010&di=f9401e64cf734ed511b080b3d5a3aea4&imgtype=jpg&src=http%3A%2F%2Fimg3.imgtn.bdimg.com%2Fit%2Fu%3D315779530%2C1004604367%26fm%3D214%26gp%3D0.jpg',
                     'https://youtu.be/aRQ0oqFBoP4'
                     )

movies = [detachment, pianist, her, romeo_must_die, transcendence, buried]
fresh_tomatoes.open_movies_page(movies)

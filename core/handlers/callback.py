from aiogram.types import CallbackQuery
from aiogram import Bot
from core.keybords.inline import get_inl_kbd_about, get_inl_kbd_why_atomy, get_inl_kbd_business, \
    get_inl_kbd_pay_company, get_inl_kbd_video, get_inl_kbd_tell, get_inl_kbd_condition_distributor, \
    get_inl_kbd_sales_repr, get_inl_kbd_agent, get_inl_kbd_dealer, get_inl_kbd_specagent, get_inl_kbd_basic, \
    get_inl_kbd_exclusive_repr, get_inl_kbd_imper_master, get_inl_kbd_kraun_master, get_inl_kbd_royal_master, \
    get_inl_kbd_sales_master, get_inl_kbd_star_master, get_inl_kbd_diamond_master, get_inl_kbd_master_qualif, \
    get_inl_kbd_sharon_master, get_inl_kbd_sponsor_reward, get_inl_kbd_products, get_inl_kbd_products_menu, \
    get_inl_kbd_condition_master, get_inl_kbd_sales_master_b, get_inl_kbd_diamond_master_b, get_inl_kbd_bonuses_master, \
    get_inl_kbd_sharon_master_b, get_inl_kbd_imper_master_b, get_inl_kbd_kraun_master_b, get_inl_kbd_royal_master_b ,\
    get_inl_kbd_star_master_b, get_inl_kbd_partner
from core.handlers.basic import get_start



async def get_about(call: CallbackQuery, bot: Bot):
    await call.message.answer(f'Atomy (Атоми) - Южно-Корейская компания, прославившаяся\n'
                         f'натуральными и безопасными продуктами для здоровья.\n'
                         f'Компания Атоми легально работает с 2009 года ми пользуется\n'
                         f'популярностью в Японии, США, Канаде, Мексике и странах\n'
                         f'Юго-Восточной Азии. А с 12 декабря 2018 года открыта и в\n'
                         f'России.\n\n'
                         f'Распространение премиум продукции повседневного спроса'
                         f'идет путем сетвого маркетинка через интернет-магазин'
                         f'Компании', reply_markup=get_inl_kbd_about())
    await call.answer()


async def get_basic(call: CallbackQuery, bot: Bot):
    await get_start(call.message, bot)
    await call.answer()


async def get_why_atomy(call: CallbackQuery, bot: Bot):
    await call.message.answer(f'В компании Atomy развита стратегия Masstige - массовость и'
                              f'престиж.'
                              f'Наш девиз: "Абсолютное качество - абсолютная цена"'
                              f'Мы используем глобальные ресурсы для глобальных продаж и'
                              f'постоянно расширяем свою линейку.'
                              f'Приверженность принципам'
                              f'Atomy соблюдает основополагающие столпы структурного'
                              f'бизнеса и всегда держит сказанное слово.'
                              f'Культура совместного роста'
                              f'Атоми помогает фирмам-партнерам производить лучшее.'
                              f'Взаимопомощь всех консультантов'
                              f'Значительная важность придается достижению успеха'
                              f'каждым участником'
                              f'«Огромный потенциал – это та компания, сотрудники и'
                              f'клиенты которой счастливы, успешны, которая вносит'
                              f'большой вклад в общество.» - Пак Хан Гиль, председатель'
                              f'Atomy.', reply_markup=get_inl_kbd_why_atomy())
    await call.answer()


async def get_business(call: CallbackQuery,  bot: Bot):
    await call.message.answer(
        '''Бизнес с "Atomy" - прекрасный шанс начать с нуля и добиваться высот, о которых прежде не мог и мечтать.
        
        Начать бизнес можно без опыта сетевого маркетинга.
        
        По статистике в нашей компании на первый Мастерский ранг самые простые люди выходят за год – полтора, а это доход уже от 100тыс руб и выше.
        
        У нас нет обязательных ежемесячных закупок,
        У нас нет необходимости заниматься продажами и что-то кому-то навязывать,
        У нас не обнуляются баллы - личные - никогда, а групповые - пока за них не получишь доход!
        Команду строим вместе!
        Что это значит? Вышестоящие наставники помогают в построении твоей структуры
        Доход получаем со всей глубины, независимо от того, кто пригласил человека – Вы, спонсор или новичок в структуре.
        
        Присоединяйтесь к нашей команде!
        Мы всегда готовы помочь!
        Готовы поделиться знаниями и научить необходимым навыкам!
    ''', reply_markup=get_inl_kbd_business())
    await call.answer()


async def get_pay_company(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''Отлично!
        
        Давай знакомиться с маркетингом!
        
        😇Как тебе будет удобнее, что бы я рассказал тебе все сам или небольшое видео с разбором маркетинга?
        ''',
        reply_markup=get_inl_kbd_pay_company()
    )
    await call.answer()


async def get_video(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''Знаешь, я еще не видел ни одного человека, который бы понял систему начислений (маркетинг-план) с первого раза.

        ⚡️В двух словах могу сказать, что в Атоми можно зарабатывать от 1200 рублей в месяц до 200 000 рублей в день.
        
        ☝️Самое важное - когда ты начнешь получать 1200 рублей, дальнейший рост твоего дохода невозможно остановить.
        
        ⚖️Компания Атоми создала схему сотрудничества, выгодную всем.
        
        Смотри видео и оцени масштаб идеи!
        
        https://youtu.be/GNXn2MZOUJo
        
        Как тебе такие варианты доходов?

        Понятное и полное объяснение?
        ''',
        reply_markup=get_inl_kbd_video()
    )

    await call.answer()


async def get_tell(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''😇С превеликим удовольствием!

        Здесь я тебе подробно расскажу обо всех ступеньках в маркетинге, какие бонусы ждут тебя на каждом этапе и объясню как перейти на следующий уровень.

        Для начала объясню тебе что такое PV.

        PV (Point Value) - это баллы, которые начисляются за покупку продукции Atomy.
        Есть личные PV, которые ты получаешь за покупку продукции для себя. А есть групповые PV, которые начисляются за покупку других людей в одной из твоих веток.

        Теперь, когда мы разобрались в терминологии, я могу рассказать тебе обо всем подробнее.

        ⬇️⬇️⬇️⬇️⬇️
        ''',
        reply_markup=get_inl_kbd_tell()
    )
    await call.answer()


async def get_condition_distributor(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔶Классификация и условия дистрибьюторства🔶

        Ниже я расположил ступени по мере возрастания товарооборота в твоей структуре.

        Посмотри какой рост может быть уже в первый месяц, два, три в твоем бизнесе!
        ''',
        reply_markup=get_inl_kbd_condition_distributor()
    )

    await call.answer()


async def get_sales_repr(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔶Торговый представитель 🔶

        💎Эта самая первая ступень твоего пути!
💡       Когда твои личные PV составляют от 10 000 PV до 299 999 PV (это от 1400 до 40000 руб), а групповой оборот меньшей ветки накопится до 300 000 PV, складывается бинарный шаг(степ), за который ты получаешь доход.
        💸Твой Чек за каждый бинарный шаг составит около 1200руб.

        💰Бинарные шаги могут проходить ежедневно!
        ''',
        reply_markup=get_inl_kbd_sales_repr()
    )
    await call.answer()


async def get_agent(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔶Агент 🔶
        
        💎Это ранг который позволяет получать за бинарный шаг сразу в 3 раза больше!!!
        
        💡Стать Агентом можно при достижении одного из условий:
        1 Личные PV >300000
        2. Накопление 600000PV в меньшей ветке за предыдущий месяц
        
        💸Твой Чек за КАЖДЫЙ бинарный шаг составит около 3600руб.
        
        💰Напомню, бинарные шаги могут проходить ежедневно!
        ''',
        reply_markup=get_inl_kbd_agent()
    )
    await call.answer()


async def get_specagent(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''
        🔶Специальный агент 🔶

        
        💎Этот статус присваивается при достижении одного из условий:
        1. Личные PV >700000
        2. Накопление 1400000PV в меньшей ветке за предыдущий месяц
        💸Твой Чек за КАЖДЫЙ бинарный шаг составит около 7200 руб.
        ''',
        reply_markup=get_inl_kbd_specagent()
    )
    await call.answer()



async def get_dealer(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''
        🔶Дилер🔶

        💎Этот статус присваивается при достижении одного из условий:
        1. Личные PV >1500000
        2. Накопление 3000000PV в меньшей ветке за предыдущий месяц
        
        💸Твой Чек за КАЖДЫЙ бинарный шаг составит около 14500 руб.
        ''',
        reply_markup=get_inl_kbd_dealer()
    )
    await call.answer()



async def get_exclusive_repr(call: CallbackQuery, bot:Bot):
    await call.message.answer(
        '''🔶Эксклюзивный дистрибьютор🔶


        💎Этот статус присваивается при достижении одного из условий:
        1. Личные PV >2400000
        2. Накопление 4800000PV в меньшей ветке за предыдущий месяц
        
        💸Твой Чек за КАЖДЫЙ бинарный шаг составит около от 21000 до 72000 руб.
        
        💰Внимание! Бинарный шаг может проходить ежедневно! Все зависит от товарооборота, который будет проходить в вашей структуре
        ''',
        reply_markup=get_inl_kbd_exclusive_repr()
    )
    await call.answer()


async def get_qualif_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Мастерское вознаграждение и квалификация мастеров🔹

        20% от общего количества PV компании распределяется между участниками согласно их уровням мастерства.
        
        ✔️Мастерское вознаграждение выплачивается два раза в месяц на 7-ой день после завершения периода подсчета. Период подсчета: с 1 по 15 число месяца, с 16 по конец месяца.
        ''',
        reply_markup=get_inl_kbd_master_qualif()
    )
    await call.answer()


async def get_sales_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Мастер продаж🔹

        Мастерское вознаграждение: 10% от общего количества PV компании распределяются только между Мастерами продаж
        
        Требования: Специальный агент с накопленными 2 500 000 PV в каждой ветке в период
        с 1 по 15/16 по конец месяца. Если количество PV в меньшей ветке более 300 000, то для достижения уровня мастерства меньшей ветке могут быть автоматически прибавлены личные PV, накопленные в период подсчета PV.

        ''',
        reply_markup=get_inl_kbd_sales_master()
    )
    await call.answer()


async def get_diamond_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Бриллиантовый мастер🔹

        Мастерское вознаграждение: 5% от общего количества PV компании распределяются между Бриллиантовыми мастерами и выше
        
        Требования: Дилер с двумя Мастерами продаж в каждой ветке
        ''',
        reply_markup=get_inl_kbd_diamond_master()
    )
    await call.answer()


async def get_sharon_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Мастер Шаронской Розы🔹

        Мастерское вознаграждение:2% от общего количества PV компании распределяются между Мастерами Шаронской Розы и выше
        
        Требования: Эксклюзивный дистрибьютор с двумя Бриллиантовыми мастерами в каждой ветке

        ''',
        reply_markup=get_inl_kbd_sharon_master()
    )
    await call.answer()


async def get_star_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Стар мастер🔹
        
        Мастерское вознаграждение: 1.2% от общего количества PV компании распределяются между Стар мастерами и выше
        
        Требования: Эксклюзивный дистрибьютор с двумя Мастерами Шаронской Розы в каждой в
        ''',
        reply_markup=get_inl_kbd_star_master()
    )
    await call.answer()


async def get_royal_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Роял мастер🔹
        
        Мастерское вознаграждение: 1% от общего количества PV компании распределяются между Роял мастерами и выше
        
        Требования: Эксклюзивный дистрибьютор с двумя Стар мастерами в каждой ветке
        ''',
        reply_markup=get_inl_kbd_royal_master()
    )
    await call.answer()


async def get_kraun_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Краун мастер🔹

        Мастерское вознаграждение: 0.5% от общего количества PV компании распределяются между Краун мастерами и выше
        
        Требования: Эксклюзивный дистрибьютор с двумя Роял мастерами в каждой ветке
        ''',
        reply_markup=get_inl_kbd_kraun_master()
    )
    await call.answer()


async def get_imper_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Империал мастер🔹

        Мастерское вознаграждение: 0.3% от общего количества PV компании распределяются между Империал мастерами и выше
        
        Требования: Эксклюзивный дистрибьютор с двумя Краун мастерами в каждой ветке

        ''',
        reply_markup=get_inl_kbd_imper_master()
    )
    await call.answer()


async def get_sponsor_reward(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔶Спонсорское вознаграждение🔶

        44% PV от общего количества PV компании распределяется между участниками согласно их уровням дистрибьюторства.
        
        🔹Вознаграждение за количество PV, накопленные в период со среды до вторника. Выплачивается на следующей неделе после завершения периода подсчета.
        
        🔹Дистрибьютор начинает накапливать групповые PV только после накопления 10 000 личных PV.
        ''',
        reply_markup=get_inl_kbd_sponsor_reward()
    )
    await call.answer()


async def get_products(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''Я с радостью расскажу о нашей продукции! 😉

        💡Продукция компании Атоми сертифицирована по международным стандартам GMP и HACCP, что обеспечивает использование лучшего сырья с соблюдением высоких требований технологического процесса и контроль на всех этапах производства.
        
        Выбери ниже, что тебе интересно и я тебе расскажу! ⬇️
        ''',
        reply_markup=get_inl_kbd_products()
    )
    await call.answer()


async def get_health(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''✅Здоровье с Atomy

        Товары для здоровья Южно-корейской Компании Атоми для всех категорий населения и всех возрастных групп.
         Здоровый образ жизни возведен жителями Южной Кореи в культ. Не удивительно, что товары, имеющие к нему непосредственное отношение, произведены по высочайшим стандартам качества. Натуральные средства от компании Atomy для здоровья и красоты:
        
        ✅Atomy красный женьшень
        ✅Аляска Е-Омега 3
        ✅Atomy Омега 3 для детей
        ✅Чай для похудения Atomy Puer Tea
        ✅Atomy Color Food Мульти витамины
        ✅Atomy Софора квин
        ✅Спирулина 
        
        😇Я хотел сделать короткое описание продукции, но ее ассортимент поистине огромен!
        
        Каталог: https://www.atomy.ru/ru/Home/Product/ProductView?GdsCode=R00001

        ''',
        reply_markup=get_inl_kbd_products_menu()
    )
    await call.answer()


async def get_hair(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''✅Уход за волосами с Atomy

        Atomy — это средства для принятия ванны и душа, а также средства по уходу за волосами, лицом и телом, разработанные специально для всех типов кожи. Натуральные активные компоненты, входящие в средства по уходу за волосами, активно воздействуют на кожу головы и волос, обеспечивая необходимую микроциркуляцию для питания волос изнутри.
        
        Для того чтобы хорошо выглядеть, необходима специальная качественная косметика для комплексного ухода за кожей лица, волосами и телом. Комплексные средства по уходу за волосами позволяют предупредить преждевременное старение волос, их выпадение.
        
        Оригинальные органические компоненты, гипоаллергенные свойства, инновационные технологии, разработанные в Южной Корее - это основные качественные преимущества продуктов компании Atomy, позволяющие ей завоёвывать всё новые и новые страны.
        
        Каталог: https://www.atomy.ru/ru/Home/Product/ProductView?GdsCode=R00001
        ''',
        reply_markup=get_inl_kbd_products_menu()
    )
    await call.answer()


async def get_leather(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''✅Уход за кожей с Atomy

        ✅Корейская органическая косметика Atomy разработана только из натуральных компонентов. Гипоаллергенная косметика подходит практически всем. Косметические средства компании Atomy зарекомендовали себя наилучшим образом.
        
        Кожа вокруг глаз особенно чувствительна, поэтому подобрать гипоаллергенный, но при этом эффективный крем — задача не из простых.
        Эффективность косметических средств Atomy доказана в ходе клинических исследований под тщательным контролем дерматологов, поэтому вы можете быть уверены, что даже сверхчувствительная кожа отреагирует на нанесение средства благоприятно.
        
        ✅Absolute CellActive Skincare - система антивозрастного ухода за кожей
        ✅Atomy SkinCare 6 system - система ухода за кожей из натуральных компонентов
        ✅Набор для глубокого увлажнения кожи Atomy Aqua
        ✅Профессиональный вечерний уход за кожей в домашних условиях Atomy Evening Care 4 Set
        
        Катало: https://www.atomy.ru/ru/Home/Product/ProductView?GdsCode=R00001

        ''',
        reply_markup=get_inl_kbd_products_menu()
    )
    await call.answer()


async def get_mouth(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''✅Зубная паста Атоми с прополисом

        👉Зубная паста с прополисом является одним из самых продаваемых товаров компании Atomy. Большинство людей, попробовав ее однажды, возвращаются за ней снова и снова.
        
        🔸Основными действующими компонентами являются экстракты зеленого чая и прополиса. Обладают антибактериальными и противовоспалительными свойствами, препятствуют размножению бактерий, предотвращают неприятный запах.
        
        🔸Так же в состав пасты входит такое вещество как ксилит, он предотвращает метаболический процесс бактерий, который является причиной появления зубного налета, уменьшает бактериальный слой на поверхности зубов.
        
        💡Важным элементом в составе пасты является фторид натрия, который защищает зубы от разрушения кислотой,  образованной бактериями зубной полости. 
        
        ⬇️Вы можете сделать заказ, нажав на кнопку ниже⬇️
        ''',
        reply_markup=get_inl_kbd_products_menu()
    )
    await call.answer()


async def get_condition_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Условия повышения уровня🔹

        Отсутствуют для уровней:
        Мастер продаж
        Бриллиантовый мастер
        Мастер Шаронской Розы
        
        Условия для уровней Стар мастер, Роял мастер, Краун мастер, Империал мастер - получить текущий уровень 3 раза.
        ''',
        reply_markup=get_inl_kbd_condition_master()
    )
    await call.answer()


async def get_bonuses_master(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Мастерское вознаграждение и квалификация мастеров🔹

        20% от общего количества PV компании распределяется между участниками согласно их уровням мастерства.
        
        ✔️Мастерское вознаграждение выплачивается два раза в месяц на 7-ой день после завершения периода подсчета. Период подсчета: с 1 по 15 число месяца, с 16 по конец месяца.
        ''',
        reply_markup=get_inl_kbd_bonuses_master()
    )
    await call.answer()


async def get_sales_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Мастер продаж"🔹

        1️⃣Атоми Скин Кеар шестиступенчатая система по уходу за кожей (1 набор)
        2️⃣Атоми ХемоХИМ (1 набор)
        3️⃣Атоми Ивнинг Кеар набор для ночного ухода из 4 средств (1 набор)
        ''',
        reply_markup=get_inl_kbd_sales_master_b()
    )
    await call.answer()


async def get_diamond_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Бриллиантовый мастер"🔹

        1️⃣Ноутбук или планшет
        2️⃣Атоми Скин Кеар шестиступенчатая система по уходу за кожей (1 набор)
        3️⃣Атоми ХемоХИМ (1 набор)
        4️⃣Атоми Ивнинг Кеар набор для ночного ухода из 4 средств (1 набор)
        ''',
        reply_markup=get_inl_kbd_diamond_master_b()
    )
    await call.answer()

async def get_sharon_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Мастер Шаронской Розы"🔹

        1️⃣Путешествие на двоих (3ночи/4дня)  👫✈️
        2️⃣Денежное вознаграждение в размере 110 тыс. руб.💰

        ''',
        reply_markup=get_inl_kbd_sharon_master_b()
    )
    await call.answer()


async def get_star_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Стар мастер"🔹


        1️⃣Путешествие на четверых (3н/4дн) 👨‍👦👩‍👧✈️
        2️⃣Денежное вознаграждение в размере 550 тыс. руб.💰💰
        ''',
        reply_markup=get_inl_kbd_star_master_b()
    )
    await call.answer()


async def get_royal_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Роял мастер"🔹

        1️⃣Путешествие на четверых (10н/11дн) 👨‍👦👫 ✈️
        2️⃣Бесплатная аренда седана бизнес класса 🚘
        3️⃣Корпоративная кредитная карта с балансом 110 тыс. руб. в месяц 💳
        4️⃣Денежное вознаграждение в размере 2,7 млн. руб. 💰💰💰

        ''',
        reply_markup=get_inl_kbd_royal_master_b()
    )
    await call.answer()


async def get_kraun_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Краун мастер"🔹

        1️⃣Путешествие на четверых (10н/11дн)👩‍👦👨‍👦
        2️⃣Бесплатная аренда седана бизнес класса🚘
        3️⃣Корпоративная кредитная карта с балансом 110 тыс. руб. в месяц 💳
        4️⃣Денежное вознаграждение в размере 2,7 млн. руб. 💰💰💰
        ''',
        reply_markup=get_inl_kbd_kraun_master_b()
    )
    await call.answer()


async def get_imper_master_b(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''🔹Поощрения для уровня "Империал мастер"🔹

        1️⃣Путешествие на четверых (10н/11дн) 👨‍👦👩‍👧✈️
        2️⃣Машина класса люкс🚘
        3️⃣Корпоративная кредитная карта с балансом 550 тыс. руб. в месяц 💳
        4️⃣Бесплатная аренда офиса площадью 165 м2 🏢
        5️⃣Личный ассистент 👩‍💼
        6️⃣Денежное вознаграждение в размере 55 млн. руб. 💰💰💰

        ''',
        reply_markup=get_inl_kbd_imper_master_b()
    )
    await call.answer()


async def get_partner(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '''😎Отлично!


        Для того, чтобы пройти регистрацию в компании, напиши моему владельцу напрямую: 
        
        @usyailek (Абязова Юлия)
        
        Он поможет тебе правильно начать свой бизнес и получать хороший результат! 
        
        💟С тобой очень приятно работать!
        
        👉Если я могу тебе еще чем-то помочь, то выбирай кнопку "Вернуться в главное меню"
        ''',
        reply_markup=get_inl_kbd_partner()
    )
    await call.answer()
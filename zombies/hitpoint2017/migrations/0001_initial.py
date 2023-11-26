# Generated by Django 1.9.4 on 2016-04-04 18:27


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("labour", "0021_auto_20160306_1125"),
    ]

    operations = [
        migrations.CreateModel(
            name="SignupExtra",
            fields=[
                (
                    "signup",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="hitpoint2017_signup_extra",
                        serialize=False,
                        to="labour.Signup",
                    ),
                ),
                (
                    "shift_type",
                    models.CharField(
                        choices=[
                            ("yksipitka", "Yksi pitk\xe4 vuoro"),
                            ("montalyhytta", "Monta lyhyemp\xe4\xe4 vuoroa"),
                            ("kaikkikay", "Kumpi tahansa k\xe4y"),
                        ],
                        help_text="Haluatko tehd\xe4 yhden pitk\xe4n ty\xf6vuoron vaiko monta lyhyemp\xe4\xe4 vuoroa?",
                        max_length=15,
                        verbose_name="Toivottu ty\xf6vuoron pituus",
                    ),
                ),
                (
                    "total_work",
                    models.CharField(
                        choices=[
                            ("8h", "Minimi - 8 tuntia"),
                            ("12h", "10\u201312 tuntia"),
                            ("yli12h", "Ty\xf6n Sankari! Yli 12 tuntia!"),
                        ],
                        help_text="Kuinka paljon haluat tehd\xe4 t\xf6it\xe4 yhteens\xe4 tapahtuman aikana? Useimmissa teht\xe4vist\xe4 minimi on kahdeksan tuntia, mutta joissain teht\xe4viss\xe4 se voi olla my\xf6s v\xe4hemm\xe4n (esim. majoitusvalvonta 6 h).",
                        max_length=15,
                        verbose_name="Toivottu kokonaisty\xf6m\xe4\xe4r\xe4",
                    ),
                ),
                (
                    "night_work",
                    models.CharField(
                        choices=[
                            ("miel", "Ty\xf6skentelen mielell\xe4ni y\xf6vuorossa"),
                            ("tarv", "Voin tarvittaessa ty\xf6skennell\xe4 y\xf6vuorossa"),
                            ("ei", "En vaan voi ty\xf6skennell\xe4 y\xf6vuorossa"),
                        ],
                        help_text="Y\xf6t\xf6it\xe4 voi olla ainoastaan lauantain ja sunnuntain v\xe4lisen\xe4 y\xf6n\xe4.",
                        max_length=5,
                        verbose_name="Voitko ty\xf6skennell\xe4 y\xf6ll\xe4?",
                    ),
                ),
                (
                    "construction",
                    models.BooleanField(
                        default=False,
                        help_text="Huomaathan, ett\xe4 perjantain ja lauantain v\xe4liselle y\xf6lle ei ole tarjolla majoitusta.",
                        verbose_name="Voin ty\xf6skennell\xe4 jo perjantaina 27. marraskuuta",
                    ),
                ),
                (
                    "overseer",
                    models.BooleanField(
                        default=False,
                        help_text="Vuorovastaavat ovat kokeneempia conity\xf6l\xe4isi\xe4, jotka toimivat oman teht\xe4v\xe4alueensa tiiminvet\xe4j\xe4n\xe4.",
                        verbose_name="Olen kiinnostunut vuorovastaavan teht\xe4vist\xe4",
                    ),
                ),
                (
                    "want_certificate",
                    models.BooleanField(
                        default=False, verbose_name="Haluan todistuksen ty\xf6skentelyst\xe4ni Hitpointissa"
                    ),
                ),
                (
                    "certificate_delivery_address",
                    models.TextField(
                        blank=True,
                        help_text="Jos haluat ty\xf6todistuksen, t\xe4yt\xe4 t\xe4h\xe4n kentt\xe4\xe4n postiosoite (katuosoite, postinumero ja postitoimipaikka) johon haluat todistuksen toimitettavan.",
                        verbose_name="Ty\xf6todistuksen toimitusosoite",
                    ),
                ),
                (
                    "special_diet_other",
                    models.TextField(
                        blank=True,
                        help_text="Jos noudatat erikoisruokavaliota, jota ei ole yll\xe4 olevassa listassa, ilmoita se t\xe4ss\xe4. Tapahtuman j\xe4rjest\xe4j\xe4 pyrkii ottamaan erikoisruokavaliot huomioon, mutta kaikkia erikoisruokavalioita ei v\xe4ltt\xe4m\xe4tt\xe4 pystyt\xe4 j\xe4rjest\xe4m\xe4\xe4n.",
                        verbose_name="Muu erikoisruokavalio",
                    ),
                ),
                (
                    "need_lodging",
                    models.BooleanField(
                        default=False,
                        verbose_name="Tarvitsen lattiamajoitusta lauantain ja sunnuntain v\xe4liseksi y\xf6ksi",
                    ),
                ),
                (
                    "prior_experience",
                    models.TextField(
                        blank=True,
                        help_text="Kerro t\xe4ss\xe4 kent\xe4ss\xe4, jos sinulla on aiempaa kokemusta vastaavista teht\xe4vist\xe4 tai muuta sellaista ty\xf6kokemusta, josta arvioit olevan hy\xf6ty\xe4 hakemassasi teht\xe4v\xe4ss\xe4.",
                        verbose_name="Ty\xf6kokemus",
                    ),
                ),
                (
                    "shift_wishes",
                    models.TextField(
                        blank=True,
                        help_text="Jos tied\xe4t nyt jo, ettet p\xe4\xe4se paikalle johonkin tiettyyn aikaan tai haluat osallistua johonkin tiettyyn ohjelmanumeroon, mainitse siit\xe4 t\xe4ss\xe4.",
                        verbose_name="Alustavat ty\xf6vuorotoiveet",
                    ),
                ),
                (
                    "free_text",
                    models.TextField(
                        blank=True,
                        help_text="Jos haluat sanoa hakemuksesi k\xe4sittelij\xf6ille jotain sellaista, jolle ei ole omaa kentt\xe4\xe4 yll\xe4, k\xe4yt\xe4 t\xe4t\xe4 kentt\xe4\xe4.",
                        verbose_name="Vapaa alue",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SpecialDiet",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="signupextra",
            name="special_diet",
            field=models.ManyToManyField(blank=True, to="hitpoint2017.SpecialDiet", verbose_name="Erikoisruokavalio"),
        ),
    ]
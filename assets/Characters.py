import dataclasses
import pathlib


@dataclasses.dataclass(frozen=True)
class Character:
    name: str
    image: str

    @property
    def image_path(self):
        """The image path"""
        return (pathlib.Path(__file__).parent / "characters" / self.image).with_suffix(
            ".png"
        )


NINGGUANG = Character("Ningguang", "character-ningguang")
KLEE = Character("Klee", "character-klee")
KAMISATO_AYAKA = Character("Kamisato Ayaka", "character-kamisato_ayaka")
YAE_MIKO = Character("Yae Miko", "character-yae_miko")
KAEDEHARA_KAZUHA = Character("Kaedehara Kazuha", "character-kaedehara_kazuha")
SANGONOMIYA_KOKOMI = Character("Sangonomiya Kokomi", "character-sangonomiya_kokomi")
DIONA = Character("Diona", "character-diona")
GOROU = Character("Gorou", "character-gorou")
ALBEDO = Character("Albedo", "character-albedo")
SAYU = Character("Sayu", "character-sayu")
SHENHE = Character("Shenhe", "character-shenhe")
JEAN = Character("Jean", "character-jean")
TRAVELER = Character("Traveler", "character-traveler")
XINYAN = Character("Xinyan", "character-xinyan")
KUJOU_SARA = Character("Kujou Sara", "character-kujou_sara")
AMBER = Character("Amber", "character-amber")
MONA = Character("Mona", "character-mona")
ZHONGLI = Character("Zhongli", "character-zhongli")
BARBARA = Character("Barbara", "character-barbara")
LISA = Character("Lisa", "character-lisa")
YUN_JIN = Character("Yun Jin", "character-yun_jin")
FISCHL = Character("Fischl", "character-fischl")
XIANGLING = Character("Xiangling", "character-xiangling")
HU_TAO = Character("Hu Tao", "character-hu_tao")
DAINSLEIF = Character("Dainsleif", "character-dainsleif")
BEIDOU = Character("Beidou", "character-beidou")
KEQING = Character("Keqing", "character-keqing")
SUCROSE = Character("Sucrose", "character-sucrose")
GANYU = Character("Ganyu", "character-ganyu")
QIQI = Character("Qiqi", "character-qiqi")
NOELLE = Character("Noelle", "character-noelle")
EULA = Character("Eula", "character-eula")
DILUC = Character("Diluc", "character-diluc")
RAIDEN_SHOGUN = Character("Raiden Shogun", "character-raiden_shogun")
THOMA = Character("Thoma", "character-thoma")
XINGQIU = Character("Xingqiu", "character-xingqiu")
VENTI = Character("Venti", "character-venti")
ARATAKI_ITTO = Character("Arataki Itto", "character-arataki_itto")
ALOY = Character("Aloy", "character-aloy")
YOIMIYA = Character("Yoimiya", "character-yoimiya")
CHONGYUN = Character("Chongyun", "character-chongyun")
KAEYA = Character("Kaeya", "character-kaeya")
YANFEI = Character("Yanfei", "character-yanfei")
XIAO = Character("Xiao", "character-xiao")
BENNETT = Character("Bennett", "character-bennett")
RAZOR = Character("Razor", "character-razor")
TARTAGLIA = Character("Tartaglia", "character-tartaglia")
ROSARIA = Character("Rosaria", "character-rosaria")


from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class BaseInfo(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=255, verbose_name="病人学籍号|身份证号")
    phone_number = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '请输入有效的手机号码')],
        verbose_name="联系电话",
        null=True, blank=True
    )
    name = models.CharField(max_length=255, verbose_name='姓名',
                            null=True, blank=True)
    gender = models.CharField(max_length=10, verbose_name='性别',
                              null=True, blank=True)
    age = models.IntegerField(
        validators=[
            MinValueValidator(1, '年龄必须大于或等于1'),
            MaxValueValidator(100, '年龄必须小于或等于100')
        ], verbose_name='年龄',
        null=True, blank=True
    )
    nation = models.CharField(max_length=255, verbose_name='民族', null=True, blank=True)
    habitation = models.CharField(max_length=255, verbose_name='居住地', null=True, blank=True)
    school = models.CharField(max_length=255, verbose_name='学校', null=True, blank=True)
    grade = models.CharField(max_length=15, verbose_name='年级', null=True, blank=True)
    screen_date = models.DateTimeField(verbose_name='诊断日期')
    glasses_worn_type = models.CharField(max_length=255, verbose_name='戴镜类型', null=True, blank=True)
    other_glasses_worn_type = models.CharField(max_length=255, verbose_name='其他戴镜类型', null=True, blank=True)

class EyeParameter(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=255, verbose_name="与其他表关联的外键")

    # region 视力
    vision_Sc_right = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='右眼裸眼视力', null=True, blank=True)
    vision_Sc_left = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='左眼裸眼视力', null=True, blank=True)
    vision_Cc_right = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='右眼戴镜视力', null=True, blank=True)
    vision_Cc_left = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='左眼戴镜视力', null=True, blank=True)
    # endregion

    # region 眼压
    intraocular_pressure_right = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='右眼眼压', null=True, blank=True)
    intraocular_pressure_left = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='左眼眼压', null=True, blank=True)
    # endregion

    # region 电脑验光结果
    computer_optometry_S_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='球镜电脑验光结果右眼', null=True, blank=True)
    computer_optometry_S_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='球镜电脑验光结果左眼', null=True, blank=True)
    computer_optometry_C_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='柱镜电脑验光结果右眼', null=True, blank=True)
    computer_optometry_C_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='柱镜电脑验光结果左眼', null=True, blank=True)
    computer_optometry_A_right = models.IntegerField(verbose_name='轴位电脑验光结果右眼', null=True, blank=True)
    computer_optometry_A_left = models.IntegerField(verbose_name='轴位电脑验光结果左眼', null=True, blank=True)
    # endregion

    # region 角膜曲率
    corneal_curvature_A = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='角膜曲率右眼R1A', null=True, blank=True)
    corneal_curvature_C = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='角膜曲率左眼R1C', null=True, blank=True)
    corneal_curvature_E = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='角膜曲率右眼R2E', null=True, blank=True)
    corneal_curvature_G = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='角膜曲率左眼R2G', null=True, blank=True)
    corneal_curvature_B = models.IntegerField(
        validators=[
            MinValueValidator(0, '角膜曲率右眼R1B必须大于或等于0'),
            MaxValueValidator(180, '角膜曲率右眼R1B必须小于或等于180')
        ],
        verbose_name='角膜曲率右眼R1B', null=True, blank=True
    )
    corneal_curvature_D = models.IntegerField(
        validators=[
            MinValueValidator(0, '角膜曲率左眼R1D必须大于或等于0'),
            MaxValueValidator(180, '角膜曲率左眼R1D必须小于或等于180')
        ],
        verbose_name='角膜曲率左眼R1D', null=True, blank=True
    )
    corneal_curvature_F = models.IntegerField(
        validators=[
            MinValueValidator(0, '角膜曲率右眼R2F必须大于或等于0'),
            MaxValueValidator(180, '角膜曲率右眼R2F必须小于或等于180')
        ],
        verbose_name='角膜曲率右眼R2F', null=True, blank=True
    )
    corneal_curvature_H = models.IntegerField(
        validators=[
            MinValueValidator(0, '角膜曲率左眼R2H必须大于或等于0'),
            MaxValueValidator(180, '角膜曲率左眼R2H必须小于或等于180')
        ],
        verbose_name='角膜曲率左眼R2H', null=True, blank=True
    )
    # endregion

    # region 筛查仪验光结果
    screen_optometry_S_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='球镜筛查仪验光结果右眼', null=True, blank=True)
    screen_optometry_S_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='球镜筛查仪验光结果左眼', null=True, blank=True)
    screen_optometry_C_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='柱镜筛查仪验光结果右眼', null=True, blank=True)
    screen_optometry_C_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='柱镜筛查仪验光结果左眼', null=True, blank=True)
    screen_optometry_A_right = models.IntegerField(verbose_name='轴位筛查仪验光结果右眼', null=True, blank=True)
    screen_optometry_A_left = models.IntegerField(verbose_name='轴位筛查仪验光结果左眼', null=True, blank=True)
    # endregion

    # region 子午-眼轴参数
    AL_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼眼轴长度', null=True, blank=True)
    AL_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼眼轴长度', null=True, blank=True)
    CCT_right = models.IntegerField(verbose_name='右眼中心角膜厚度', null=True, blank=True)
    CCT_left = models.IntegerField(verbose_name='左眼中心角膜厚度', null=True, blank=True)
    ACD_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼前房深度', null=True, blank=True)
    ACD_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼前房深度', null=True, blank=True)
    LT_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼晶体厚度', null=True, blank=True)
    LT_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼晶体厚度', null=True, blank=True)
    VCD_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼玻璃体腔长度', null=True, blank=True)
    VCD_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼玻璃体腔长度', null=True, blank=True)
    PD_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼瞳孔直径', null=True, blank=True)
    PD_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼瞳孔直径', null=True, blank=True)
    WTW_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼角膜直径', null=True, blank=True)
    WTW_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼角膜直径', null=True, blank=True)
    # endregion

    # region 屈光参数
    refractive_SE_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼屈光参数SE', null=True, blank=True)
    refractive_SE_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼屈光参数SE', null=True, blank=True)
    refractive_A = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数右眼R1A', null=True, blank=True)
    refractive_C = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数左眼R1C', null=True, blank=True)
    refractive_E = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数右眼R2E', null=True, blank=True)
    refractive_G = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数左眼R2G', null=True, blank=True)
    refractive_I = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数右眼K1I', null=True, blank=True)
    refractive_K = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数左眼K1K', null=True, blank=True)
    refractive_M = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数右眼K2M', null=True, blank=True)
    refractive_O = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='屈光参数左眼K2O', null=True, blank=True)
    refractive_B = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数右眼R1B必须大于或等于0'),
            MaxValueValidator(180, '屈光参数右眼R1B必须小于或等于180')
        ],
        verbose_name='屈光参数右眼R1B', null=True, blank=True
    )
    refractive_D = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数左眼R1D必须大于或等于0'),
            MaxValueValidator(180, '屈光参数左眼R1D必须小于或等于180')
        ],
        verbose_name='屈光参数左眼R1D', null=True, blank=True
    )
    refractive_F = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数右眼R2F必须大于或等于0'),
            MaxValueValidator(180, '屈光参数右眼R2F必须小于或等于180')
        ],
        verbose_name='屈光参数右眼R2F', null=True, blank=True
    )
    refractive_H = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数左眼R2H必须大于或等于0'),
            MaxValueValidator(180, '屈光参数左眼R2H必须小于或等于180')
        ],
        verbose_name='屈光参数左眼R2H', null=True, blank=True
    )
    refractive_J = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数右眼K1J必须大于或等于0'),
            MaxValueValidator(180, '屈光参数右眼K1J必须小于或等于180')
        ],
        verbose_name='屈光参数右眼K1J', null=True, blank=True
    )
    refractive_L = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数左眼K1L必须大于或等于0'),
            MaxValueValidator(180, '屈光参数左眼K1L必须小于或等于180')
        ],
        verbose_name='屈光参数左眼K1L', null=True, blank=True
    )
    refractive_N = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数右眼K2N必须大于或等于0'),
            MaxValueValidator(180, '屈光参数右眼K2N必须小于或等于180')
        ],
        verbose_name='屈光参数右眼K2N', null=True, blank=True
    )
    refractive_P = models.IntegerField(
        validators=[
            MinValueValidator(0, '屈光参数左眼K2P必须大于或等于0'),
            MaxValueValidator(180, '屈光参数左眼K2P必须小于或等于180')
        ],
        verbose_name='屈光参数左眼K2P', null=True, blank=True
    )
    # endregion

    # region 矫正眼压
    correcting_intraocular_pressure_right = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='右眼矫正眼压', null=True, blank=True)
    correcting_intraocular_pressure_left = models.DecimalField(max_digits=9, decimal_places=1, verbose_name='左眼矫正眼压', null=True, blank=True)
    # endregion

    # region 角膜中央最薄点厚度
    thinnest_center_thickness_right = models.IntegerField(verbose_name='右眼角膜中央最薄点厚度', null=True, blank=True)
    thinnest_center_thickness_left = models.IntegerField(verbose_name='左眼角膜中央最薄点厚度', null=True, blank=True)
    # endregion

    # region 角膜定点形变幅度的比值
    DA_ratio_one_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼1mm角膜定点形变幅度的比值', null=True, blank=True)
    DA_ratio_one_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼1mm角膜定点形变幅度的比值', null=True, blank=True)
    DA_ratio_two_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼2mm角膜定点形变幅度的比值', null=True, blank=True)
    DA_ratio_two_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼2mm角膜定点形变幅度的比值', null=True, blank=True)
    # endregion

    # region 厚度变化率
    ARTh_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼厚度变化率', null=True, blank=True)
    ARTh_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼厚度变化率', null=True, blank=True)
    # endregion

    # region 综合半径
    IR_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼综合半径', null=True, blank=True)
    IR_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼综合半径', null=True, blank=True)
    # endregion

    # region 角膜硬度参数
    SP_A1_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼角膜硬度参数', null=True, blank=True)
    SP_A1_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼角膜硬度参数', null=True, blank=True)
    # endregion

    # region 生物力学参数
    CBI_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼生物力学参数', null=True, blank=True)
    CBI_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼生物力学参数', null=True, blank=True)
    # endregion

    # region 应力应变参数
    SSI_right = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='右眼应力应变参数', null=True, blank=True)
    SSI_left = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='左眼应力应变参数', null=True, blank=True)
    # endregion

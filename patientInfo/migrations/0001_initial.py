# Generated by Django 5.1.1 on 2025-02-22 09:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseInfo",
            fields=[
                (
                    "patient_id",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="病人学籍号|身份证号",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=11,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^1[3-9]\\d{9}$", "请输入有效的手机号码"
                            )
                        ],
                        verbose_name="联系电话",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="姓名")),
                ("gender", models.CharField(max_length=10, verbose_name="性别")),
                (
                    "age",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1, "年龄必须大于或等于1"),
                            django.core.validators.MaxValueValidator(
                                100, "年龄必须小于或等于100"
                            ),
                        ],
                        verbose_name="年龄",
                    ),
                ),
                (
                    "nation",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="民族"
                    ),
                ),
                (
                    "habitation",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="居住地"
                    ),
                ),
                (
                    "school",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="学校"
                    ),
                ),
                (
                    "grade",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="年级"
                    ),
                ),
                ("screen_date", models.DateTimeField(verbose_name="诊断日期")),
                (
                    "glasses_worn_type",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="戴镜类型"
                    ),
                ),
                (
                    "other_glasses_worn_type",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="其他戴镜类型"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EyeParameter",
            fields=[
                (
                    "patient_id",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="与其他表关联的外键",
                    ),
                ),
                (
                    "vision_Sc_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼裸眼视力",
                    ),
                ),
                (
                    "vision_Sc_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼裸眼视力",
                    ),
                ),
                (
                    "vision_Cc_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼戴镜视力",
                    ),
                ),
                (
                    "vision_Cc_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼戴镜视力",
                    ),
                ),
                (
                    "intraocular_pressure_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼眼压",
                    ),
                ),
                (
                    "intraocular_pressure_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼眼压",
                    ),
                ),
                (
                    "computer_optometry_S_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="球镜电脑验光结果右眼",
                    ),
                ),
                (
                    "computer_optometry_S_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="球镜电脑验光结果左眼",
                    ),
                ),
                (
                    "computer_optometry_C_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="柱镜电脑验光结果右眼",
                    ),
                ),
                (
                    "computer_optometry_C_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="柱镜电脑验光结果左眼",
                    ),
                ),
                (
                    "computer_optometry_A_right",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="轴位电脑验光结果右眼"
                    ),
                ),
                (
                    "computer_optometry_A_left",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="轴位电脑验光结果左眼"
                    ),
                ),
                (
                    "corneal_curvature_A",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="角膜曲率右眼R1A",
                    ),
                ),
                (
                    "corneal_curvature_C",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="角膜曲率左眼R1C",
                    ),
                ),
                (
                    "corneal_curvature_E",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="角膜曲率右眼R2E",
                    ),
                ),
                (
                    "corneal_curvature_G",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="角膜曲率左眼R2G",
                    ),
                ),
                (
                    "corneal_curvature_B",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "角膜曲率右眼R1B必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "角膜曲率右眼R1B必须小于或等于180"
                            ),
                        ],
                        verbose_name="角膜曲率右眼R1B",
                    ),
                ),
                (
                    "corneal_curvature_D",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "角膜曲率左眼R1D必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "角膜曲率左眼R1D必须小于或等于180"
                            ),
                        ],
                        verbose_name="角膜曲率左眼R1D",
                    ),
                ),
                (
                    "corneal_curvature_F",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "角膜曲率右眼R2F必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "角膜曲率右眼R2F必须小于或等于180"
                            ),
                        ],
                        verbose_name="角膜曲率右眼R2F",
                    ),
                ),
                (
                    "corneal_curvature_H",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "角膜曲率左眼R2H必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "角膜曲率左眼R2H必须小于或等于180"
                            ),
                        ],
                        verbose_name="角膜曲率左眼R2H",
                    ),
                ),
                (
                    "screen_optometry_S_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="球镜筛查仪验光结果右眼",
                    ),
                ),
                (
                    "screen_optometry_S_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="球镜筛查仪验光结果左眼",
                    ),
                ),
                (
                    "screen_optometry_C_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="柱镜筛查仪验光结果右眼",
                    ),
                ),
                (
                    "screen_optometry_C_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="柱镜筛查仪验光结果左眼",
                    ),
                ),
                (
                    "screen_optometry_A_right",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="轴位筛查仪验光结果右眼"
                    ),
                ),
                (
                    "screen_optometry_A_left",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="轴位筛查仪验光结果左眼"
                    ),
                ),
                (
                    "AL_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼眼轴长度",
                    ),
                ),
                (
                    "AL_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼眼轴长度",
                    ),
                ),
                (
                    "CCT_right",
                    models.IntegerField(blank=True, null=True, verbose_name="右眼中心角膜厚度"),
                ),
                (
                    "CCT_left",
                    models.IntegerField(blank=True, null=True, verbose_name="左眼中心角膜厚度"),
                ),
                (
                    "ACD_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼前房深度",
                    ),
                ),
                (
                    "ACD_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼前房深度",
                    ),
                ),
                (
                    "LT_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼晶体厚度",
                    ),
                ),
                (
                    "LT_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼晶体厚度",
                    ),
                ),
                (
                    "VCD_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼玻璃体腔长度",
                    ),
                ),
                (
                    "VCD_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼玻璃体腔长度",
                    ),
                ),
                (
                    "PD_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼瞳孔直径",
                    ),
                ),
                (
                    "PD_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼瞳孔直径",
                    ),
                ),
                (
                    "WTW_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼角膜直径",
                    ),
                ),
                (
                    "WTW_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼角膜直径",
                    ),
                ),
                (
                    "refractive_SE_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼屈光参数SE",
                    ),
                ),
                (
                    "refractive_SE_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼屈光参数SE",
                    ),
                ),
                (
                    "refractive_A",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数右眼R1A",
                    ),
                ),
                (
                    "refractive_C",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数左眼R1C",
                    ),
                ),
                (
                    "refractive_E",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数右眼R2E",
                    ),
                ),
                (
                    "refractive_G",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数左眼R2G",
                    ),
                ),
                (
                    "refractive_I",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数右眼K1I",
                    ),
                ),
                (
                    "refractive_K",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数左眼K1K",
                    ),
                ),
                (
                    "refractive_M",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数右眼K2M",
                    ),
                ),
                (
                    "refractive_O",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="屈光参数左眼K2O",
                    ),
                ),
                (
                    "refractive_B",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数右眼R1B必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数右眼R1B必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数右眼R1B",
                    ),
                ),
                (
                    "refractive_D",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数左眼R1D必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数左眼R1D必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数左眼R1D",
                    ),
                ),
                (
                    "refractive_F",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数右眼R2F必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数右眼R2F必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数右眼R2F",
                    ),
                ),
                (
                    "refractive_H",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数左眼R2H必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数左眼R2H必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数左眼R2H",
                    ),
                ),
                (
                    "refractive_J",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数右眼K1J必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数右眼K1J必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数右眼K1J",
                    ),
                ),
                (
                    "refractive_L",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数左眼K1L必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数左眼K1L必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数左眼K1L",
                    ),
                ),
                (
                    "refractive_N",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数右眼K2N必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数右眼K2N必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数右眼K2N",
                    ),
                ),
                (
                    "refractive_P",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(
                                0, "屈光参数左眼K2P必须大于或等于0"
                            ),
                            django.core.validators.MaxValueValidator(
                                180, "屈光参数左眼K2P必须小于或等于180"
                            ),
                        ],
                        verbose_name="屈光参数左眼K2P",
                    ),
                ),
                (
                    "correcting_intraocular_pressure_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼矫正眼压",
                    ),
                ),
                (
                    "correcting_intraocular_pressure_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼矫正眼压",
                    ),
                ),
                (
                    "thinnest_center_thickness_right",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="右眼角膜中央最薄点厚度"
                    ),
                ),
                (
                    "thinnest_center_thickness_left",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="左眼角膜中央最薄点厚度"
                    ),
                ),
                (
                    "DA_ratio_one_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼1mm角膜定点形变幅度的比值",
                    ),
                ),
                (
                    "DA_ratio_one_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼1mm角膜定点形变幅度的比值",
                    ),
                ),
                (
                    "DA_ratio_two_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼2mm角膜定点形变幅度的比值",
                    ),
                ),
                (
                    "DA_ratio_two_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼2mm角膜定点形变幅度的比值",
                    ),
                ),
                (
                    "ARTh_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼厚度变化率",
                    ),
                ),
                (
                    "ARTh_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼厚度变化率",
                    ),
                ),
                (
                    "IR_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼综合半径",
                    ),
                ),
                (
                    "IR_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼综合半径",
                    ),
                ),
                (
                    "SP_A1_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼角膜硬度参数",
                    ),
                ),
                (
                    "SP_A1_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼角膜硬度参数",
                    ),
                ),
                (
                    "CBI_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼生物力学参数",
                    ),
                ),
                (
                    "CBI_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼生物力学参数",
                    ),
                ),
                (
                    "SSI_right",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="右眼应力应变参数",
                    ),
                ),
                (
                    "SSI_left",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                        verbose_name="左眼应力应变参数",
                    ),
                ),
            ],
        ),
    ]

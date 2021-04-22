from django.db import models

# Create your models here.

DEPT_CHOICES = (('运营部','运营部'),('技术部','技术部'),('人事行政部部','人事行政部部'),('客服部','客服部'),('财务部','财务部'),)
EMP_STATUS_CHOICES = (('在职','在职'),('辞职','辞职'),('辞退','辞退'),('自离','自离'),)
EMP_TYPE_CHOICES = (('正式员工','正式员工'),('实习生','实习生'),('兼职','兼职'),('其他','其他'),)
EXIST_CHOICES = (('有','有'),('无','无'),)
GENDER_CHOICES = (('男','男'),('女','女'),('其他','其他'),)

class Employee(models.Model):
    empno = models.CharField(unique=True, max_length=100, blank=True, null=True, verbose_name= '工号')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name= '姓名')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name= '邮件')
    status = models.CharField(choices=EMP_STATUS_CHOICES,max_length=100, blank=True, null=True, verbose_name='人员状态')
    emptype = models.CharField(choices=EMP_TYPE_CHOICES,max_length=100, blank=True, null=True, verbose_name='人员类别')
    contract_corp = models.CharField(max_length=100, blank=True, null=True, verbose_name= '合同签约分公司')
    office_city = models.CharField(max_length=100, blank=True, null=True, verbose_name= '办公区域')

    dept1 = models.CharField(choices=DEPT_CHOICES, max_length=100, blank=True, null=True, verbose_name= '部门1')
    dept2 = models.CharField(choices=DEPT_CHOICES, max_length=100, blank=True, null=True, verbose_name= '部门2')

    position = models.CharField(max_length=100, blank=True, null=True, verbose_name= '岗位名称')
    enroll_date = models.CharField(max_length=100, blank=True, null=True, verbose_name= '入职日期')
    gender = models.CharField(choices=GENDER_CHOICES,max_length=100, blank=True, null=True, verbose_name='性别')
    nation = models.CharField(max_length=100, blank=True, null=True, verbose_name= '民族')
    native_place = models.CharField(max_length=100, blank=True, null=True, verbose_name= '籍贯')
    birth_date = models.CharField(max_length=100, blank=True, null=True, verbose_name= '出生日期')
    edu_degree = models.CharField(max_length=100, blank=True, null=True, verbose_name= '学历')
    edu_school = models.CharField(max_length=100, blank=True, null=True, verbose_name= '毕业院校')
    edu_major = models.CharField(max_length=100, blank=True, null=True, verbose_name= '专业')
    edu_graduate_date = models.CharField(max_length=100, blank=True, null=True, verbose_name= '毕业日期')
    mobile = models.CharField(max_length=100, blank=True, null=True, verbose_name= '手机')
    wechat = models.CharField(max_length=100, blank=True, null=True, verbose_name= 'wechat')
    created_date = models.CharField(max_length=100, blank=True, null=True, verbose_name= '数据录入时间')
    updated_date = models.CharField(max_length=100, blank=True, null=True, verbose_name= '数据更新时间')
    comment = models.CharField(max_length=100, blank=True, null=True, verbose_name= '备注')

    class Meta:
        verbose_name =  u'员工'
        verbose_name_plural = u'花名册'